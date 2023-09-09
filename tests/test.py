import pdb
import sys
import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .pages import (BasePage, FindOwnersPage, HomePage, NewOwnerPage,
                    OwnerInformationPage, OwnersPage, VeterinariansPage)

debugger = pdb.Pdb(skip=["altwalker.*"], stdout=sys.stdout)
fake = Faker()

HEADLESS = False
BASE_URL = "http://127.0.0.1:8080/"

driver = None


def setUpRun():
    """Setup the webdriver."""

    global driver

    options = Options()
    if HEADLESS:
        options.add_argument("-headless")

    print("Create a new Firefox session")
    driver = webdriver.Firefox(options=options)

    print("Set implicitly wait")
    driver.implicitly_wait(1)
    print("Window size: {width}x{height}".format(**driver.get_window_size()))


def tearDownRun():
    """Close the webdriver."""

    global driver

    print("Close the Firefox session")
    driver.quit()


class BaseModel(unittest.TestCase):
    """Contains common methods for all models."""

    def setUpModel(self):
        global driver
        print("Set up for: {}".format(type(self).__name__))
        self.driver = driver

    def v_HomePage(self):
        page = HomePage(self.driver)
        self.assertEqual(page.heading_text, "Welcome", "Welcome heading should be present")
        self.assertTrue(page.is_footer_present, "Footer should be present")

    def v_FindOwners(self):
        page = FindOwnersPage(self.driver)
        self.assertEqual("Find Owners",page.heading_text, "Find Owners heading should be present")
        self.assertTrue(page.is_footer_present, "Footer should be present")

    def v_NewOwner(self):
        page = NewOwnerPage(self.driver)
        self.assertEqual("Owner", page.heading_text, "Owner heading should be present")
        self.assertTrue(page.is_footer_present, "Footer should be present")

    def v_Owners(self):
        page = OwnersPage(self.driver)
        self.assertEqual("Owners", page.heading_text, "Owners heading should be present")
        self.assertGreaterEqual(page.total_owners_in_list, 5, "Owners in listing >= 5")

    def v_Veterinarians(self):
        page = VeterinariansPage(self.driver)
        self.assertEqual(page.heading_text, "Veterinarians", "Veterinarians heading should be present")
        self.assertTrue(page.is_footer_present, "Footer should be present")

    def v_OwnerInformation(self, data):
        page = OwnerInformationPage(self.driver)
        self.assertEqual(page.heading_text, "Owner Information", "Owner Information heading should be present")
        data["numOfPets"] = page.number_of_pets
        print(f"numOfPets: {page.number_of_pets}")
        self.assertTrue(page.is_footer_present, "Footer should be present")

    def e_DoNothing(self, data):
        # debugger.set_trace()
        pass

    def e_FindOwners(self):
        page = BasePage(self.driver)
        page.click_find_owners()


class PetClinic(BaseModel):

    def e_StartBrowser(self):
        self.page = HomePage(self.driver, BASE_URL)
        self.page.open()

    def e_HomePage(self):
        self.page.click_home()

    def e_Veterinarians(self):
        self.page.click_veterinarians()

    def e_FindOwners(self):
        self.page.click_find_owners()


class FindOwners(BaseModel):

    def setUpModel(self):
        super().setUpModel()
        self.page = FindOwnersPage(self.driver)

    def e_AddOwner(self):
        self.page.click_add_owner()

    def e_Search(self):
        self.page.click_submit()


class OwnerInformation(BaseModel):

    def setUpModel(self):
        super().setUpModel()
        self.page = OwnerInformationPage(self.driver)

    def e_UpdatePet(self):
        self.page.click_submit()

    def e_AddPetSuccessfully(self):
        self.page.fill_out_pet_info(name=fake.name(), birth_date=fake.past_date(), type="dog")
        self.page.click_submit()

    def e_AddPetFailed(self):
        self.page.fill_out_pet_info(birth_date=fake.past_date(), type="dog")
        self.page.click_submit()

    def e_AddNewPet(self):
        self.page.click_add_new_pet()

    def e_EditPet(self):
        self.page.click_edit_pet()

    def e_AddVisit(self):
        self.page.click_add_visit()

    def v_NewPet(self):
        self.assertEqual(self.page.heading_text, "New Pet", "New Pet heading should be present")
        self.assertTrue(self.page.is_footer_present, "Footer should be present")

    def v_NewVisit(self):
        self.assertEqual(self.page.heading_text, "New Visit", "New Visit heading should be present")

    def e_VisitAddedSuccessfully(self):
        self.page.clear_description()
        self.page.set_description(fake.name())
        self.page.click_submit()

    def e_VisitAddedFailed(self):
        self.page.clear_description()
        self.page.click_submit()

    def v_Pet(self):
        self.assertEqual(self.page.heading_text, "Pet", "Pet heading should be present")


class Veterinarians(BaseModel):

    def v_Veterinarians(self):
        page = VeterinariansPage(self.driver)
        self.assertEqual(page.heading_text, "Veterinarians", "Veterinarians heading should be present")
        self.assertGreater(page.number_of_vets_in_table, 0, "At least one Veterinarian should be listed in table")


class NewOwner(BaseModel):

    def setUpModel(self):
        super().setUpModel()
        self.page = NewOwnerPage(self.driver)

    def e_CorrectData(self):
        self.page.fill_owner_data(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), city=fake.city(), telephone=fake.pystr_format('##########'))
        self.page.click_submit()

    def e_IncorrectData(self):
        self.page.fill_owner_data()
        self.page.fill_telephone(fake.pystr_format('####################'))
        self.page.click_submit()

    def v_IncorrectData(self):
        self.assertTrue(self.page.error_message, "numeric value out of bounds (<10 digits>.<0 digits> expected")
