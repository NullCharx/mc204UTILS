package es.nullbyte.charmiscmods.datagen.tempaux;

import java.util.Optional;
import java.util.concurrent.CompletableFuture;
import net.minecraft.core.Cloner;
import net.minecraft.core.HolderLookup;
import net.minecraft.core.RegistryAccess;
import es.nullbyte.charmiscmods.datagen.tempaux.RegistrySetBuilder;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.data.registries.VanillaRegistries;
import net.minecraft.resources.RegistryDataLoader;
import net.minecraft.world.level.biome.Biome;
import net.minecraft.world.level.levelgen.placement.PlacedFeature;

public class RegistryPatchGenerator {
    public static CompletableFuture<RegistrySetBuilder.PatchedRegistries> createLookup(CompletableFuture<HolderLookup.Provider> p_310881_, RegistrySetBuilder p_310262_) {
        return p_310881_.thenApply((p_309945_) -> {
            RegistryAccess.Frozen registryaccess$frozen = RegistryAccess.fromRegistryOfRegistries(BuiltInRegistries.REGISTRY);
            Cloner.Factory cloner$factory = new Cloner.Factory();
            net.minecraftforge.registries.DataPackRegistriesHooks.getDataPackRegistriesWithDimensions().forEach(registryData -> registryData.runWithArguments(cloner$factory::addCodec));
            RegistrySetBuilder.PatchedRegistries registrysetbuilder$patchedregistries = p_310262_.buildPatch(registryaccess$frozen, p_309945_, cloner$factory);
            HolderLookup.Provider holderlookup$provider = registrysetbuilder$patchedregistries.full();
            Optional<HolderLookup.RegistryLookup<Biome>> optional = holderlookup$provider.lookup(Registries.BIOME);
            Optional<HolderLookup.RegistryLookup<PlacedFeature>> optional1 = holderlookup$provider.lookup(Registries.PLACED_FEATURE);
            if (optional.isPresent() || optional1.isPresent()) {
                VanillaRegistries.validateThatAllBiomeFeaturesHaveBiomeFilter(optional1.orElseGet(() -> {
                    return p_309945_.lookupOrThrow(Registries.PLACED_FEATURE);
                }), optional.orElseGet(() -> {
                    return p_309945_.lookupOrThrow(Registries.BIOME);
                }));
            }

            return registrysetbuilder$patchedregistries;
        });
    }
}
