#/usr/bin/python3
def convert_to_climate_parameter_list(biomes_data):
    # Function to format a single parameter or a range of parameters
    def format_parameter_range(min_val, max_val):
        if min_val == max_val:
            return f"Climate.Parameter.point({min_val}F)"
        else:
            return f"Climate.Parameter.span({min_val}F, {max_val}F)"

    # List to store formatted strings for each biome's parameters
    climate_parameters_list = []

    # Iterating through each biome entry
    for biome in biomes_data:
        namespace, biome_name = biome["biome"].split(":")
        
        # Check if biome is from Minecraft or a mod
        biome_source = "Biomes" if namespace == "minecraft" else "ModBiomes" #Change this to the name of the class that holds our custom biomes

        # Formatting each parameter
        temperature = format_parameter_range(*params["temperature"])
        humidity = format_parameter_range(*params["humidity"])
        continentalness = format_parameter_range(*params["continentalness"])
        erosion = format_parameter_range(*params["erosion"])
        weirdness = format_parameter_range(*params["weirdness"])
        depth = format_parameter_range(*params["depth"])  # Depth is always a single value
        offset = params["offset"]  # Offset is a single float value

        # Constructing the string for this biome's parameters
        parameters_str = f"Climate.parameters({temperature}, {humidity}, {continentalness}, {erosion}, {weirdness}, {depth}, {offset}F)"
        climate_parameters_list.append(f"Pair.of({parameters_str}, biomeRegistry.getOrThrow(Biomes.{biome_name}))")

    # Joining all the biome parameter strings into the final Java code format for Climate.ParameterList
    climate_parameter_list_java_code = f"new Climate.ParameterList<>(List.of(\n    " + ',\n'.join(climate_parameters_list) + "\n));"

    return climate_parameter_list_java_code

# Example biome data (without the dimension header)
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
    }
]

# You can call the function with your biome data to get the Java code

print(convert_to_climate_parameter_list(biomes_data))
