# Dictionary storing subscription plans and their details
PLANS = {
    "free": {"price": 0.00, "features": "Ads, shuffle-only play, standard audio"},
    "individual": {"price": 17.90, "features": "No ads, offline downloads, high audio quality"},
    "duo": {"price": 23.90, "features": "2 Premium accounts, Duo Mix playlist"},
    "family": {"price": 29.90, "features": "Up to 6 accounts, parental controls"},
    "student": {"price": 8.95, "features": "Premium features, discounted rate"},
}

def get_plan_details(plan):
    # Retrieve plan details, converting input to lowercase to avoid case sensitivity issues
    return PLANS.get(plan.lower())

def calculate_annual_cost(monthly_price):
    # Calculate the total cost 1 year 
    return monthly_price * 12

def compare_plans():
    # Format and display all available plans with their monthly and annual costs
    lines = []
    lines.append(f"{'Plan':<12} {'Monthly':<10} {'Annual (RM)':<12} {'Features'}")
    lines.append("-" * 75)
    for name, info in PLANS.items():
        annual = calculate_annual_cost(info['price'])
        lines.append(f"{name.title():<12} RM{info['price']:<8.2f} RM{annual:<10.2f} {info['features']}")
    return "\n".join(lines)

def calculate_plan_change(current_plan, new_plan):
    # Calculate the price difference when upgrading or downgrading between plans
    current = get_plan_details(current_plan)
    new = get_plan_details(new_plan)
    if not current or not new:
        return "Invalid plan(s) selected."
    diff = new["price"] - current["price"]
    if diff > 0:
        return f"Upgrading from {current_plan} to {new_plan} costs RM{diff:.2f} more per month."
    elif diff < 0:
        return f"Downgrading from {current_plan} to {new_plan} saves RM{abs(diff):.2f} per month."
    else:
        return "Same price — no change in cost."

