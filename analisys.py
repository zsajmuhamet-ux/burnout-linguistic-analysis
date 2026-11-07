import numpy as np
import scipy.stats as stats

def run_fisher_test(marker_name, group_a_count, group_a_total, group_b_count, group_b_total):
    """
    Performs Fisher's Exact Test for a linguistic marker between Burnout (A) and Control (B) groups.
    """
    # Constructing a 2x2 contingency table
    table = np.array([
        [group_a_count, group_a_total - group_a_count],
        [group_b_count, group_b_total - group_b_count]
    ])
    
    odds_ratio, p_value = stats.fisher_exact(table)
    
    print(f"--- Marker: {marker_name} ---")
    print(f"Group A (Burnout) Rate: {(group_a_count / group_a_total) * 1000:.1f}‰")
    print(f"Group B (Control) Rate: {(group_b_count / group_b_total) * 1000:.1f}‰")
    print(f"P-value: {p_value:.5f}")
    print(f"Statistically Significant (p < 0.05): {p_value < 0.05}\n")

if __name__ == "__main__":
    print("Executing Statistical Validation for Burnout Markers...\n")
    
    # Total tokens in sample slices
    TOTAL_A = 3800  # Burnout tokens sample
    TOTAL_B = 3253  # Control tokens sample
    
    # 1. Obligation Modality (Significant)
    run_fisher_test("Obligation Modality", 15, TOTAL_A, 1, TOTAL_B)
    
    # 2. 'Can't / Cannot' Constructions (Significant)
    run_fisher_test("Can't/Cannot Constraints", 8, TOTAL_A, 0, TOTAL_B)
    
    # 3. First-Person Singular Pronouns (Not Significant)
    run_fisher_test("First-Person Pronouns", 352, TOTAL_A, 310, TOTAL_B)
  
