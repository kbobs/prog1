frequency = float(input("What is the frequency of the radiation? "))

if frequency<3e9:
    print("The electromagnetic radiation is radio waves.")
elif frequency>=3e9 and frequency<3e12:
    print("The electromagnetic radiation is microwaves.")
elif frequency>=3e12 and frequency<4.3e14:
    print("The electromagnetic radiation is infared light.")
elif frequency>=4.3e14 and frequency<7.5e14:
    print("The electromagnetic radiation is visible light.")
elif frequency>=7.5e14 and frequency<3e17:
    print("The electromagnetic radiation is ultraiolet light.")
elif frequency>=3e17 and frequency<3e19:
    print("The electromagnetic radiation is X-rays.")
elif frequency>=3e19:
    print("The electromagnetic radiation is gamma rays.")
else:
    print("Please enter a valid frequency range.")
