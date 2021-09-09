import pandas as pd

df = pd.read_csv("~/Documents/code/misc-data/ts_2020.csv")

variables = [
    "V201005",  # political interest
    "V201006",  # campaign interest
    "V201013a",  # state
    "V201033",  # vote intention cand
    "V201200",  # self-placement
    "V201217",  # vote exp
    "V201218",  # close race
    "V201231x",  # party_id
    "V201377",  # trust media
    "V201433",  # trust media
    "V201507x",  # age
    "V201511x",  # educ
    "V201549x",  # race
    "V201600",  # sex
    "V201617x",  # income
    "V202072",  # voted in 2020
    "V202161",  # feel lib
    "V202164",  # feel con
    "V202541a",  # facebook
    "V202541b",  # twitter
    "V202541c",  # instagram
    "V202541d",  # reddit
    "V202541e",  # youtube
    "V202542",  # how often fb
    "V202543",  # how often fb pol
    "V202544",  # how often tw
    "V202545",  # how often tw pol
    "V202546",  # how often rd
    "V202547",  # how often rd pol
    "V203003",  # region
]

var_names = {
    "V201005": "political_int",
    "V201006": "campaign_int",
    "V201013a": "state",
    "V201033": "vote intention cand",
    "V201200": "self-placement",
    "V201217": "vote_exp",
    "V201218": "close_race",
    "V201231x": "party_id",
    "V201377": "trust_media",
    "V201433": "religion",
    "V201507x": "age",
    "V201511x": "educ",
    "V201549x": "race",
    "V201600": "sex",
    "V201617x": "income",
    "V202072": "vote_2020",
    "V202161": "feel_lib",
    "V202164": "feel_con",
    "V202541a": "facebook",
    "V202541b": "twitter",
    "V202541c": "instagram",
    "V202541d": "reddit",
    "V202541e": "youtube",
    "V202542": "freq_fb",
    "V202543": "freq_fb pol",
    "V202544": "freq_tw",
    "V202545": "freq_tw pol",
    "V202546": "freq_rd",
    "V202547": "freq_rd pol",
    "V203003": "region",
}

df = df[variables].rename(columns=var_names)

df[['freq_fb pol', 'state' ]].groupby('state').mean()

.counts()


# Loading a raw dataset, transforming it, and saving it into a clean dataset
  filter(
    age >= 18,
    between(gender, 1, 3),
    between(income, 1, 16),
    education > 0,
    between(voting_int, 1, 4),
    between(party_id, 1, 3),
    between(ideology, 1, 7),
    between(religion, 1, 2),
    between(pres_appr, 1, 2),
    between(sexism, 1, 3),
    between(latino, 1, 2),
    feeling_dem >= 0,
    feeling_rep >= 0,
  ) %>%
  mutate(
    date       = as_date(date),
    gender     = factor(gender,  labels = c("Male", "Female", "Other")),
    region     = factor(region,  labels = c("Northeast", "Midwest", "South", "West")),
    voting_int = factor(voting_int, labels = c("H. Clinton", "D. Trump", "G. Johnson", "J. Stein")),
    party_id   = factor(party_id, labels = c("Democrat", "Republican", "Independent")),
    religion   = factor(religion, labels = c("Important", "Not important")),
    pres_appr  = factor(pres_appr, labels = c("Approve", "Disapprove")),
    sexism     = factor(sexism, labels = c("Better", "Worse", "Makes no difference")),
    latino     = factor(latino, labels = c("Yes", "No")),
  ) %>%
  saveRDS("clean_2016.rds")
