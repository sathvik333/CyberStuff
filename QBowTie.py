import matplotlib.pyplot as plt
import numpy as np

# Sample threats
threats = {
    'Hacker': 0.27,
    'Malware': 0.18,
    'Insider': 0.15,
    'Lost Device': 0.12,
    'Vulnerabilities': 0.08
}

# Sample barriers
hacker_barriers = {'Firewall': 4, 'Encryption': 5, 'Training': 2}
malware_barriers = {'Antivirus': 3, 'Web Filter': 4, 'Training': 5}
insider_barriers = {'Access Control': 4, 'Monitoring': 3, 'Training': 2}
lost_device_barriers = {'Remote Wipe': 3, 'Encryption': 4, 'Training': 2}
vulnerabilities_barriers = {'Patch Management': 4, 'Security Testing': 3, 'Training': 2}

# Sample escalators
hacker_escalators = {'Sensitive Data': 4, 'Cloud Migration': 2, 'Outsourcing': 3}
insider_escalators = {'Data Exfiltration': 3, 'Privilege Escalation': 2, 'Unauthorized Access': 3}
lost_device_escalators = {'Data Exposure': 3, 'Unauthorized Access': 2, 'Physical Theft': 3}
vulnerabilities_escalators = {'Exploitation': 4, 'Public Disclosure': 3, 'Unpatched Systems': 2}

# Sample consequences
consequences = {
    'Business Interrupt': 0.33,
    'Financial Loss': 0.22,
    'Reputation': 0.25,
    'Regulatory': 0.15
}

# Sample consequence barriers
biz_interrupt_barriers = {'BCP': 5, 'Recovery': 4, 'Auditing': 3}
financial_loss_barriers = {'Insurance': 4, 'Risk Management': 3, 'Contingency Planning': 4}
reputation_barriers = {'Crisis Management': 4, 'Public Relations': 4, 'Transparency': 3}
regulatory_barriers = {'Compliance': 5, 'Audit Preparedness': 3, 'Legal Counsel': 4}

# Sample consequence escalators
biz_interrupt_escalators = {'IT Critical': 4, 'IT Reliance': 5}
financial_loss_escalators = {'Market Conditions': 4, 'Economic Factors': 3}
reputation_escalators = {'Media Coverage': 3, 'Social Media Impact': 4}
regulatory_escalators = {'Government Actions': 5, 'Industry Regulations': 4}

def get_weighted_scores(scores):
    total = sum(scores.values())
    return {k: v/total for k, v in scores.items()}

def get_barrier_score(threats, barriers):
    barrier_scores = {}
    for t, v in threats.items():
        if t in barriers:
            barrier_scores[t] = get_weighted_scores(barriers[t])
    return barrier_scores

def get_escalator_score(threats, escalators):
    escalator_scores = {}
    for t, v in threats.items():
        if t in escalators:
            escalator_scores[t] = get_weighted_scores(escalators[t])
    return escalator_scores

barrier_scores = get_barrier_score(threats, {
    'Hacker': hacker_barriers,
    'Malware': malware_barriers,
    'Insider': insider_barriers,
    'Lost Device': lost_device_barriers,
    'Vulnerabilities': vulnerabilities_barriers
})

escalator_scores = get_escalator_score(threats, {
    'Hacker': hacker_escalators,
    'Insider': insider_escalators,
    'Lost Device': lost_device_escalators,
    'Vulnerabilities': vulnerabilities_escalators
})

def get_likelihood(threats, barrier_scores, escalator_scores, residual_risk=0.2):
    likelihoods = []
    for t, threat_value in threats.items():
        threat_contrib = threat_value * (1 - residual_risk)
        if t in barrier_scores:
            barrier_effect = sum(v for k, v in barrier_scores[t].items())
        else:
            barrier_effect = 0
        if t in escalator_scores:
            escalator_effect = sum(v for k, v in escalator_scores[t].items()) / 3
        else:
            escalator_effect = 0
        likelihood = threat_contrib * (barrier_effect - escalator_effect)
        likelihoods.append(likelihood)
    return sum(likelihoods)

likelihood = get_likelihood(threats, barrier_scores, escalator_scores)

def get_severity(consequences, barrier_scores, escalator_scores, residual_risk=0.2):
    severities = []
    for c, consequence_value in consequences.items():
        consequence_contrib = consequence_value * (1 - residual_risk)
        if c in barrier_scores:
            barrier_effect = sum(v for k, v in barrier_scores[c].items())
        else:
            barrier_effect = 0
        if c in escalator_scores:
            escalator_effect = sum(v for k, v in escalator_scores[c].items()) / 3
        else:
            escalator_effect = 0
        severity = consequence_contrib * (barrier_effect - escalator_effect)
        severities.append(severity)
    return sum(severities)

severity = get_severity(consequences, {
    'Business Interrupt': biz_interrupt_barriers,
    'Financial Loss': financial_loss_barriers,
    'Reputation': reputation_barriers,
    'Regulatory': regulatory_barriers
}, {
    'Business Interrupt': biz_interrupt_escalators,
    'Financial Loss': financial_loss_escalators,
    'Reputation': reputation_escalators,
    'Regulatory': regulatory_escalators
})

# Risk matrix
risk_matrix = {
    (1, 1): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4, (1, 5): 5,
    (2, 1): 2, (2, 2): 4, (2, 3): 6, (2, 4): 8, (2, 5): 10,
    (3, 1): 3, (3, 2): 6, (3, 3): 9, (3, 4): 12, (3, 5): 15,
    (4, 1): 4, (4, 2): 8, (4, 3): 12, (4, 4): 16, (4, 5): 20,
    (5, 1): 5, (5, 2): 10, (5, 3): 15, (5, 4): 20, (5, 5): 25
}

# Map likelihood and severity to risk matrix
likelihood_rating = 3
severity_rating = 2
cyber_risk_rating = risk_matrix[(likelihood_rating, severity_rating)]

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Add threats
for i, (t, v) in enumerate(threats.items()):
    ax.annotate(t, xy=(0.1, 0.8 - i * 0.1), fontsize=14)

# Add barriers
for i, (t, barrier_dict) in enumerate(barrier_scores.items()):
    for j, (b, v) in enumerate(barrier_dict.items()):
        ax.annotate(b, xy=(0.2 + j * 0.1, 0.8 - i * 0.1), fontsize=10)

# Add escalators
for i, (t, escalator_dict) in enumerate(escalator_scores.items()):
    for j, (e, v) in enumerate(escalator_dict.items()):
        ax.annotate(e, xy=(0.7 + j * 0.1, 0.8 - i * 0.1), fontsize=10)

# Add consequences
for i, (c, v) in enumerate(consequences.items()):
    ax.annotate(c, xy=(0.5, 0.1 + i * 0.1), fontsize=14, ha='center')

# Add consequence barriers
y = 0.2
for c, barrier_dict in barrier_scores.items():
    for b in barrier_dict:
        ax.annotate(b, xy=(0.4, y), fontsize=10, ha='right')
        y += 0.1

# Add consequence escalators
y = 0.2
for c, escalator_dict in escalator_scores.items():
    for e in escalator_dict:
        ax.annotate(e, xy=(0.6, y), fontsize=10, ha='left')
        y += 0.1

# Set axes off
ax.axis('off')

# Show plot
plt.show()

print("Likelihood:", likelihood)
print("Severity:", severity)
print("Cyber Risk Rating:", cyber_risk_rating)
