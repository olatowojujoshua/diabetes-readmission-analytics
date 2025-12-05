surv_select_df = diabetes_surv_df.select(
    "event_early_readmit",
    "time_to_event",
    "age",
    "gender",
    "time_in_hospital",
    "num_lab_procedures",
    "num_medications",
    "number_inpatient",
    "admission_type_desc"
)

surv_pd = surv_select_df.sample(fraction=0.20, seed=42).toPandas()
surv_pd.head()

from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

kmf = KaplanMeierFitter()

T = surv_pd["time_to_event"]         # time variable
E = surv_pd["event_early_readmit"]   # event indicator

plt.figure(figsize=(8,6))
kmf.fit(T, event_observed=E)
kmf.plot_survival_function()

plt.title("Kaplan–Meier Survival Curve for Early Readmission")
plt.xlabel("Days")
plt.ylabel("Survival Probability (No Early Readmission)")
plt.grid(True)
plt.show()

surv_pd["age"] = surv_pd["age"].astype(str)
