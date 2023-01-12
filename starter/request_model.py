from enum import Enum
from pydantic import BaseModel


class WorkClass(str, Enum):
    Private = 'Private'
    Self_emp_not_inc = 'Self-emp-not-inc'
    Local_gov = 'Local-gov'
    Question = '?'
    State_gov = 'State-gov'
    Self_emp_inc = 'Self-emp-inc'
    Federal_gov = 'Federal-gov'
    Without_pay = 'Without-pay'
    Never_worked = 'Never-worked'


class Education(str, Enum):
    Bachelors = 'Bachelors'
    Some_college = 'Some-college'
    Eleventh = '11th'
    HS_grad = 'HS-grad'
    Prof_school = 'Prof-school'
    Assoc_acdm = 'Assoc-acdm'
    Assoc_voc = 'Assoc-voc'
    Ninth = '9th'
    Seventh_eight = '7th-8th'
    Twelfth = '12th'
    Masters = 'Masters'
    First_fourth = '1st-4th'
    Tenth = '10th'
    Doctorate = 'Doctorate'
    Fifth_sixth = '5th-6th'
    Preschool = 'Preschool'


class MaritalStatus(str, Enum):
    Married_civ_spouse = 'Married-civ-spouse'
    Divorced = 'Divorced'
    Never_married = 'Never-married'
    Separated = 'Separated'
    Widowed = 'Widowed'
    Married_spouse_absent = 'Married-spouse-absent'
    Married_AF_spouse = 'Married-AF-spouse'

class Occupation(str, Enum):
    Tech_support = 'Tech-support'
    Craft_repair = 'Craft-repair'
    Other_service = 'Other-service'
    Sales = 'Sales'
    Exec_managerial = 'Exec-managerial'
    Prof_specialty = 'Prof-specialty'
    Handlers_cleaners = 'Handlers-cleaners'
    Machine_op_inspct = 'Machine-op-inspct'
    Adm_clerical = 'Adm-clerical'
    Farming_fishing = 'Farming-fishing'
    Transport_moving = 'Transport-moving'
    Priv_house_serv = 'Priv-house-serv'
    Protective_serv = 'Protective-serv'
    Armed_Forces = 'Armed-Forces'

class Relationship(str, Enum):
    Wife = 'Wife'
    Own_child = 'Own-child'
    Husband = 'Husband'
    Not_in_family = 'Not-in-family'
    Other_relative = 'Other-relative'
    Unmarried = 'Unmarried'

class Race(str, Enum):
    White = 'White'
    Asian_Pac_Islander = 'Asian-Pac-Islander'
    Amer_Indian_Eskimo = 'Amer-Indian-Eskimo'
    Other = 'Other'
    Black = 'Black'

class Sex(str, Enum):
    Male = 'Male'
    Female = 'Female'

class NativeCountry(str, Enum):
    United_States = 'United-States'
    Cambodia = 'Cambodia'
    England = 'England'
    Puerto_Rico = 'Puerto-Rico'
    Canada = 'Canada'
    Germany = 'Germany'
    Outlying_US_Guam_USVI_etc = 'Outlying-US(Guam-USVI-etc)'
    India = 'India'
    Japan = 'Japan'
    Greece = 'Greece'
    South = 'South'
    China = 'China'
    Cuba = 'Cuba'
    Iran = 'Iran'
    Honduras = 'Honduras'
    Philippines = 'Philippines'
    Italy = 'Italy'
    Poland = 'Poland'
    Jamaica = 'Jamaica'
    Vietnam = 'Vietnam'
    Mexico = 'Mexico'
    Portugal = 'Portugal'
    Ireland = 'Ireland'
    France = 'France'
    Dominican_Republic = 'Dominican-Republic'
    Laos = 'Laos'
    Ecuador = 'Ecuador'
    Taiwan = 'Taiwan'
    Haiti = 'Haiti'
    Columbia = 'Columbia'
    Hungary = 'Hungary'
    Guatemala = 'Guatemala'
    Nicaragua = 'Nicaragua'
    Scotland = 'Scotland'
    Thailand = 'Thailand'
    Yugoslavia = 'Yugoslavia'
    El_Salvador = 'El-Salvador'
    Trinadad_Tobago = 'Trinadad&Tobago'
    Peru = 'Peru'
    Hong = 'Hong'
    Holand_Netherlands = 'Holand-Netherlands'


def to_minus_case(string: str) -> str:
    return string.replace("_", "-")


class Input(BaseModel):
    age: int
    workclass: WorkClass
    fnlwgt: int
    education: Education
    education_num: int
    marital_status: MaritalStatus
    occupation: Occupation
    relationship: Relationship
    race: Race
    sex: Sex
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: NativeCountry

    class Config:
        # with this config, we can convert the input's keys to minus case
        alias_generator = to_minus_case

        # with this config, we can get the enum's value instead of the enum's name on calling dict() method
        use_enum_values = True