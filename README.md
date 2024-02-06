# DPBEPFIX
DatapackBuiltinEntriesProvider fix for 1.20.2+ for those who want to use it after someone deleted the class without warning or alternatives

If you have been following tutorials like Kaupenjoe's about ore generations or otherwise used the missing class but have found that in 1.20.2+ DataPackBuiltinEntriesProvider class is missing, it is because someone decided to delete as "it was of no use in their opinion"
There is an open pull request with the solution -although someone is also hetistant on making it onto the live branch- here: https://github.com/MinecraftForge/MinecraftForge/pull/9848

To make it work in the meantime, you have to use the missing class DataPackEntriesProvider, as well as two other classes which need to be patched: RegistrypatchGenerator and RegistrySetBuilder. The class itself and the patches are in the commit, but if you are lazy or unable of applying the patches by yourself, you have the three java classes in this repository.
You only have to ddrop them in your mod and change any reference to the classes in your worldgen data generators to this classes. It won't affect MC or Forge functionality as it won't override net.minecraft.core classes.
