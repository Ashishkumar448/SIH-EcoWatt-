from random import choice

tips = [
    "Turn off lights when you leave a room—unless you enjoy paying for electricity you're not using.",
    "Unplug devices when not in use; your phone charger doesn’t need a break, but your wallet does.",
    "Switch to LED bulbs—they’re bright, just like your idea to save money.",
    "Use a power strip for your gadgets and flip the switch off—because vampires aren't the only ones who drain energy.",
    "Wash clothes in cold water; your washing machine isn’t trying to make soup.",
    "Set your thermostat a little higher in summer; your house doesn't need to be an ice palace.",
    "Turn off lights when not in use.",
    "Unplug electronics when they're not being used.",
    "Use energy-efficient appliances.",
    "Opt for natural lighting during the day.",
    "Insulate your home to reduce heating and cooling costs.",
    "Switch to LED light bulbs.",
    "Consider a programmable thermostat.",
    "Seal windows and doors to prevent drafts.",
    "Use cold water for laundry when possible.",
    "Maintain your HVAC system regularly."
]

def get_tip():
    return choice(tips)