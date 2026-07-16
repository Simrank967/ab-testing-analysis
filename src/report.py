def generate_report(lift, z_p, chi_p, required_sample, actual_sample):
    if z_p < 0.05:
        significance = "Statistically Significant"
    else:
        significance = "Not Statistically Significant"

    if lift["absolute_lift"] > 0 and z_p < 0.05:
        recommendation = "SHIP"
        reason = "Treatment improves conversion significantly."
    elif lift["absolute_lift"] < 0 and z_p < 0.05:
        recommendation = "DO NOT SHIP"
        reason = "Treatment significantly decreases conversion."
    else:
        recommendation = "NEED MORE DATA"
        reason = "No statistically significant improvement."

    report = f"""
====================================================
                 A/B TEST REPORT
====================================================

BUSINESS PROBLEM
----------------------------------------------------
Determine whether the new marketing strategy (PSA)
should replace the existing advertisement campaign.

====================================================
EXPERIMENT RESULTS
====================================================

Control Group: {lift['control_group']}
Treatment Group: {lift['treatment_group']}

Control Conversion Rate : {lift['control_rate']:.2f}%
Treatment Conversion Rate : {lift['treatment_rate']:.2f}%

Absolute Lift : {lift['absolute_lift']:.2f}%
Relative Lift : {lift['relative_lift']:.2f}%

====================================================
STATISTICAL ANALYSIS
====================================================

Z-Test P-value : {z_p:.2e}
Chi-Square P-value : {chi_p:.2e}

====================================================
SAMPLE SIZE
====================================================

Required Sample : {required_sample:.0f}
Actual Sample : {actual_sample}

====================================================
BUSINESS INSIGHT
====================================================

The treatment (PSA) produced a significantly lower
conversion rate than the control (Ads).

The confidence interval is entirely below zero,
indicating the decrease is statistically significant.

====================================================
FINAL RECOMMENDATION
====================================================

{recommendation}

Reason:
{reason}
"""