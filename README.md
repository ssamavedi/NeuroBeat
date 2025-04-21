# Concussion Detection via Heart Rate Variability (HRV) Using Machine Learning

## Introduction

Each year, approximately 3.8 million athletes suffer from concussions, with 19% of athletes in contact sports at risk of sustaining one per year (1). Concussions are traumatic brain injuries caused by a blow to the head (2). Unfortunately, up to half of concussions go undetected, putting athletes at risk for repeated concussions, which may lead to Chronic Traumatic Encephalopathy (CTE) (3,4). Studies have found that 92% of ex-NFL players show signs of CTE, leading to progressive memory decline, depression, aggression, and dementia (5).

The current standard of care for diagnosing concussions on-site, the SCAT5 (Sport Concussion Assessment Tool 5), has limitations in sensitivity, objectivity, and specificity. It relies heavily on subjective tests and self-reported symptoms (3-9), increasing the risk of undiagnosed CTE (3,4). Studies have shown varied test-retest reliability of SCAT5, ranging from 20% to 52% sensitivity and 21% to 91% specificity (7-8). Moreover, athletes may intentionally withhold symptoms to avoid being removed from play (9).

### Objective

To address these challenges, we developed a machine learning tool that uses heart rate variability (HRV) as a biomarker for concussion diagnosis. HRV is linked to autonomic nervous system (ANS) dysregulation, which can occur after a concussion (12-16). Our tool uses commercially available heart rate monitors to track HRV during play, comparing real-time HRV measurements to baseline data to detect concussions on-site.

## Materials and Methods

### Training & Development of Classifier

Our machine learning algorithm was trained using publicly available datasets from Physionet: Healthy RR, CEBSDB, and CHARIS (N=601). We developed a pre-processing pipeline to standardize ECG data from different sources, including steps to locate RR intervals and remove noise artifacts. We extracted several key HRV features from the RR interval data, such as:

- Range
- IQR (Interquartile Range)
- Variance
- Standard Deviation
- Coefficient of Variance

The classifier uses logistic regression with a 75% training and 25% testing split, resulting in 451 training samples and 150 testing samples.

### Data Collection

To evaluate the classifier’s performance, we conducted experiments with 15 collegiate athletes (ages 20 ± 2) using the Frontier X2 ECG system. Athletes underwent baseline testing both at rest and during physical activity. After baseline testing, we conducted both TBI (traumatic brain injury) and non-TBI perturbation tests to simulate real-world conditions. The collected data (N=30 samples) was then used to test the algorithm’s ability to differentiate between concussed and healthy states.

## Results

### Model Performance

NeuroBeat's logistic regression classifier achieved an accuracy rate of **89.33%** on the training data, with cross-validation yielding an average accuracy of **~86%** (Table 4, Fig 2). The model uses standard deviation as a key feature to distinguish between concussed and healthy individuals (Fig 3.1), supporting the hypothesis that HRV changes in response to concussion.

### Testing with Collected Data

When tested on the data we collected from 15 athletes (N=30), the classifier achieved **83.33% accuracy** with a **17.2% false positive rate**. The confidence threshold was set to 50%. Standard deviation was found to be the most important feature in classifying concussed versus healthy states (Fig 4).

These promising results suggest that HRV may provide a reliable physiological marker for concussion detection. Further research, including IRB-approved studies, is needed to refine the algorithm and reduce false positives and negatives.

## Conclusions and Future Work

The results indicate that HRV-based concussion detection has potential as a non-invasive, real-time tool for identifying concussions on-site. Future work will involve collecting more data, particularly from concussed individuals, to enhance the classifier’s sensitivity and specificity. Additionally, we plan to optimize the algorithm by determining the best thresholds for minimizing false positives and negatives.

## Acknowledgements

Our work was conducted under the guidance of **Dr. Ross Venook**, Senior Lecturer in Bioengineering at Stanford University. We were funded by the **Biodesign NEXT grant**, awarded through the **Stanford Byers Center for Biodesign**.

## References

1. Centers for Disease Control and Prevention. (n.d.). [Press release](https://www.cdc.gov/media/pressrel/2007/r070607.htm).
2. Centers for Disease Control and Prevention. (2019, February 12). [What is a concussion?](https://www.cdc.gov/headsup/basics/concussion_whatis.html)
3. Galgano, M. A., Cantu, R., & Chin, L. S. (2016). Chronic traumatic encephalopathy: The impact on athletes. *Cureus*. [Link](https://doi.org/10.7759/cureus.532)
4. Mez, J., et al. (2017). Clinicopathological evaluation of chronic traumatic encephalopathy in players of American football. *JAMA*, 318(4), 360. [Link](https://doi.org/10.1001/jama.2017.8334)
5. Researchers find CTE in 345 of 376 former NFL players studied. [Link](https://www.bumc.bu.edu/busm/2023/02/06/researchers-find-cte-in-345-of-376-former-nfl-players-studied/)
6. Petit, K. M., et al. (2020). The Sport Concussion Assessment Tool-5 (SCAT5): Baseline assessments in NCAA Division I collegiate student-athletes. *International Journal of Exercise Science*. [Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7449330/)
7. Hänninen, T., et al. (2021). Reliability of the sport concussion assessment tool 5 baseline testing: A 2-week test–retest study. *Journal of Science and Medicine in Sport*, 24(2), 129–134. [Link](https://doi.org/10.1016/j.jsams.2020.07.014)
8. Harmon, K. G., et al. (2022). Diagnostic accuracy and reliability of sideline concussion evaluation: A prospective, case-controlled study in college athletes comparing newer tools and established tests. *British Journal of Sports Medicine*. [Link](https://bjsm.bmj.com/content/56/3/144.long)

