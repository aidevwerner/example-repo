# example-repo

## Financial Calculator

This repository contains a Python program that allows users to perform one of two financial calculations:

- **Investment interest calculator** — computes returns on an investment using either simple or compound interest.
- **Home loan repayment calculator** — determines the monthly repayment amount on a home loan.

---

## Background

### What is Interest?

Interest appears in almost every financial transaction — whether you are taking out a loan (and paying extra back to the bank) or making an investment (and earning more over time). There are two main types of interest:

### Simple Interest

Simple interest is calculated solely on the **principal amount** (the initial amount invested or borrowed), once per year. Each year, the same fixed interest amount is added.

**Example:**
Investing H$1,000 at 10% simple interest:
- Year 1: H$1,000 × 0.10 = H$100 interest → Total: **H$1,100**
- Year 2: H$1,000 × 0.10 = H$100 interest → Total: **H$1,200**

### Compound Interest

Compound interest is calculated on the **accumulated amount** (principal + previously earned interest), so your returns grow faster over time.

**Example:**
Investing H$1,000 at 10% compound interest:
- Year 1: H$1,000 × 0.10 = H$100 interest → Accumulated: **H$1,100**
- Year 2: H$1,100 × 0.10 = H$110 interest → Accumulated: **H$1,210**

---

## Features

- Calculate the final return on an investment using **simple** or **compound** interest
- Calculate the **monthly repayment** amount on a home loan
- Interactive command-line interface

---

## Getting Started

### Prerequisites

- Python 3.x

### Running the Program

```bash
git clone https://github.com/aidevwerner/example-repo.git
cd example-repo
python finance_calculator.py
```

---

## Usage

On launch, the program will prompt you to choose between:

1. **Investment** — Enter your principal, interest rate, number of years, and interest type (simple or compound).
2. **Bond (Home Loan)** — Enter the property value, annual interest rate, and number of months to repay.

