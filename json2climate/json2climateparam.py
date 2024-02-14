#/usr/bin/python3
def convert_to_climate_parameter_list(biomes_data):
    # Function to format a single parameter or a range of parameters
    def format_parameter_range(value):
        if isinstance(value, list): #If the parameter is a list, the result is a Climate.parameter.span
            min_val, max_val = value
            return f"Climate.Parameter.span({min_val}F, {max_val}F)" if min_val != max_val else f"Climate.Parameter.point({min_val}F)"
        else: #If not Climate.parameter.point
            return f"Climate.Parameter.point({value}F)"

    # List to store formatted strings for each biome's parameters
    climate_parameters_list = []

    # Iterating through each biome entry
    for biome in biomes_data:
        namespace, biome_name = biome["biome"].split(":")
        
        # Check if biome is from Minecraft or a mod
        biome_source = "Biomes" if namespace == "minecraft" else "ModBiomes"

        params = biome["parameters"]

        # Formatting each parameter
        temperature = format_parameter_range(params["temperature"])
        humidity = format_parameter_range(params["humidity"])
        continentalness = format_parameter_range(params["continentalness"])
        erosion = format_parameter_range(params["erosion"])
        weirdness = format_parameter_range(params["weirdness"])
        depth = format_parameter_range(params.get("depth", 0))
        offset = f"{params['offset']}F"  # Offset is always a single float value

        # Constructing the string for this biome's parameters
        parameters_str = f"Climate.parameters({temperature}, {humidity}, {continentalness}, {erosion}, {weirdness}, {depth}, {offset})"
        biome_constant = f"{biome_source}.{biome_name.upper()}"
        climate_parameters_list.append(f"Pair.of({parameters_str}, {biome_constant})")

    # Joining all the biome parameter strings into the final Java code format for Climate.ParameterList
    climate_parameter_list_java_code = f"new Climate.ParameterList<>(List.of(\n    " + ',\n    '.join(climate_parameters_list) + "\n));"

    return climate_parameter_list_java_code

biomes_data = [
    {
        "biome": "minecraft:grove",
        "parameters": {
            "temperature": [-0.15, 0.2],
            "humidity": [0.3, 1],
            "continentalness": [-0.11, 1],
            "erosion": [-1, -0.7799],
            "weirdness": [-1, -0.9333],
            "depth": 0,
            "offset": 0
        }
    },
    {
        "biome": "minecraft:grove",
        "parameters": {
            "temperature": [-0.15, 0.2],
            "humidity": [0.3, 1],
            "continentalness": [-0.11, 1],
            "erosion": [-1, -0.7799],
            "weirdness": [-1, -0.9333],
            "depth": 1,
            "offset": 0
        }
    },
    {
        "biome": "relativedimensions:aberant_forest",
        "parameters": {
            "temperature": [-0.15, 0.2],
            "humidity": [0.3, 1],
            "continentalness": [-0.11, 1],
            "erosion": [-1, -0.7799],
            "weirdness": [-1, -0.9333],
            "depth": 1,
            "offset": 0
        }
    }
]

print(convert_to_climate_parameter_list(biomes_data))

