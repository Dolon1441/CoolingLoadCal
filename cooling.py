def calculate_cooling_load(area, num_occupants, building_type, outdoor_temp, indoor_desired_temp):
    if building_type == "residential":
        cooling_load = 100 * num_occupants
    elif building_type == "commercial":
        cooling_load = 150 * num_occupants
    else:
        print("Invalid building type. Supported types: residential, commercial")
        return None

    overall_heat_transfer_coefficient = 30  # W/m²°C

    # Calculate heat transfer due to conduction
    q_conduction = overall_heat_transfer_coefficient * area * (outdoor_temp - indoor_desired_temp)

    # Calculate the sensible cooling load
    sensible_cooling_load = q_conduction + cooling_load

    return sensible_cooling_load

def main():
    print("Cooling Load Calculator")

    try:
        area = float(input("Enter the area of the building in square meters: "))
        num_occupants = int(input("Enter the number of occupants in the building: "))
        building_type = input("Enter the type of building (residential, commercial, etc.): ").lower()
        outdoor_temp = float(input("Enter the outdoor temperature in Celsius: "))
        indoor_desired_temp = float(input("Enter the indoor desired temperature in Celsius: "))

        cooling_load = calculate_cooling_load(area, num_occupants, building_type, outdoor_temp, indoor_desired_temp)

        if cooling_load is not None:
            print(f"\nThe sensible cooling load for the building is {cooling_load:.2f} W.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
