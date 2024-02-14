function convertJSON() {
    const jsonInput = document.getElementById("jsonInput").value;
    try {
        const biomesData = JSON.parse(jsonInput);
        const output = []; // This will store the output strings
        
        biomesData.forEach(biome => {
            const params = biome.parameters;
            const temperature = formatParameterRange(params.temperature);
            const humidity = formatParameterRange(params.humidity);
            const continentalness = formatParameterRange(params.continentalness);
            const erosion = formatParameterRange(params.erosion);
            const weirdness = formatParameterRange(params.weirdness);
            const depth = formatParameterRange(params.depth);
            const offset = `${params.offset}F`;

            const biomeNamespace = biome.biome.includes("minecraft:") ? "Biomes" : "ModBiomes";
            const biomeName = biome.biome.split(":")[1].toUpperCase();

            output.push(`Pair.of(Climate.parameters(${temperature}, ${humidity}, ${continentalness}, ${erosion}, ${weirdness}, ${depth}, ${offset}), ${biomeNamespace}.${biomeName})`);
        });

        document.getElementById("output").textContent = `new Climate.ParameterList<>(List.of(\n ${output.join(',\n ')} \n));`;
    } catch (e) {
        document.getElementById("output").textContent = "Invalid JSON input.";
    }
}

function formatParameterRange(range) {
    if (Array.isArray(range)) {
        return range[0] === range[1] ? `Climate.Parameter.point(${range[0]}F)` : `Climate.Parameter.span(${range[0]}F, ${range[1]}F)`;
    }
    return `Climate.Parameter.point(${range}F)`;
}
