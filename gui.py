import tkinter as tk
import autoplay


def start_function():
    selected_options = []
    if bulletin_board_var.get():
        selected_options.append("Bulletin Board")
    if daily_login_shop_var.get():
        selected_options.append("Daily Login Shop")
    if send_friend_points_var.get():
        selected_options.append("Send Friend Points")
    if claim_outpost_defense_var.get():
        selected_options.append("Claim Outpost Defense")
    if general_shop_var.get():
        selected_options.append("General Shop")
    if arena_shop_var.get():
        selected_options.append("Arena Shop")
    if claim_special_rewards_var.get():
        selected_options.append("Claim Special Rewards")
    if simulation_room_var.get():
        selected_options.append("Simulation Room")
    if tribe_tower_var.get():
        selected_options.append("Tribe Tower")

    # Call the different function with the selected options
    call_function(selected_options)
    return


def call_function(selected_options):
    print("Selected Options:")
    for option in selected_options:
        print(option)
    autoplay.playGame(selected_options)


# Create the GUI window
window = tk.Tk()
window.title("Options Selector")

# Create the checkbox variables
bulletin_board_var = tk.IntVar(value=1)
daily_login_shop_var = tk.IntVar(value=1)
send_friend_points_var = tk.IntVar(value=1)
claim_outpost_defense_var = tk.IntVar(value=1)
general_shop_var = tk.IntVar(value=1)
arena_shop_var = tk.IntVar(value=1)
claim_special_rewards_var = tk.IntVar(value=1)
simulation_room_var = tk.IntVar(value=1)
tribe_tower_var = tk.IntVar(value=1)

# Create the checkboxes
bulletin_board_checkbox = tk.Checkbutton(
    window, text="Bulletin Board", variable=bulletin_board_var
)
bulletin_board_checkbox.pack()

daily_login_shop_checkbox = tk.Checkbutton(
    window, text="Daily Login Shop", variable=daily_login_shop_var
)
daily_login_shop_checkbox.pack()

send_friend_points_checkbox = tk.Checkbutton(
    window, text="Send Friend Points", variable=send_friend_points_var
)
send_friend_points_checkbox.pack()

claim_outpost_defense_checkbox = tk.Checkbutton(
    window, text="Claim Outpost Defense", variable=claim_outpost_defense_var
)
claim_outpost_defense_checkbox.pack()

general_shop_checkbox = tk.Checkbutton(
    window, text="General Shop", variable=general_shop_var
)
general_shop_checkbox.pack()

arena_shop_checkbox = tk.Checkbutton(window, text="Arena Shop", variable=arena_shop_var)
arena_shop_checkbox.pack()

claim_special_rewards_checkbox = tk.Checkbutton(
    window, text="Claim Special Rewards", variable=claim_special_rewards_var
)
claim_special_rewards_checkbox.pack()

simulation_room_checkbox = tk.Checkbutton(
    window, text="Simulation Room", variable=simulation_room_var
)
simulation_room_checkbox.pack()

tribe_tower_checkbox = tk.Checkbutton(
    window, text="Tribe Tower", variable=tribe_tower_var
)
tribe_tower_checkbox.pack()

# Create the Start button
start_button = tk.Button(window, text="Start", command=start_function)
start_button.pack()

# Run the GUI loop
window.mainloop()
