# Section 9: PROJECT-SPECIFIC CONCEPTS - Logistic Regression (Binary Classification)

In the previous project, we predicted a continuous number (Price). In this project, we predict a **Category** (e.g., Yes/No, 0/1, Spam/Not Spam).

### The Math: Sigmoid Function
Instead of a straight line, we use a curve that squashes all numbers between 0 and 1. This is called the **Sigmoid** function:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Where $z = w \cdot x + b$.

### Real-World Analogy
Predicting survival is like a light switch with a dimmer. The switch outputs a probability (e.g., "70% chance of survival"), and we decide if it's "On" (Survive) or "Off" (Die) based on a threshold (usually 0.5).
