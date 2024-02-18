This is now a repository of tools I've made during the oddysey it's being getting up to date with Forge 1.20.4 modding. Below is a list with all the utilities in their respective folders:

# DPBEPFIX
DatapackBuiltinEntriesProvider fix for 1.20.2+ for those who want to use it after someone deleted the class without warning or alternatives

If you have been following tutorials like Kaupenjoe's about ore generations or otherwise used the missing class but have found that in 1.20.2+ DataPackBuiltinEntriesProvider class is missing, it is because someone decided to delete as "it was of no use in their opinion"
There is an open pull request with the solution -although someone is also hetistant on making it onto the live branch- here: https://github.com/MinecraftForge/MinecraftForge/pull/9848

To make it work in the meantime, you have to use the missing class DataPackEntriesProvider, as well as two other classes which need to be patched: RegistrypatchGenerator and RegistrySetBuilder. The class itself and the patches are in the commit, but if you are lazy or unable of applying the patches by yourself, you have the three java classes in this repository.
You only have to ddrop them in your mod and change any reference to the classes in your worldgen data generators to this classes. It won't affect MC or Forge functionality as it won't override net.minecraft.core classes.
**As of 49.0.30 DatapackBuiltinEntriesProvider has been readded to forge. Just delete your custom folder an point all the dangling referneces back to the mc core library after updating**

# JSON2Climate
I've found myself wanting to make a dimension identical to  the overworld with added biomes. Of course, adding biomes cant be done in the default overworld but there is a workaround, copying the dimension generation json in its entirety for a new dimension. The problem is that it has+ 7k biome entries. So, after following Kaupenjoe's dimension tutorial, i've made this little tool that can convert any dimension json biomes list to a java list of Climate settings reddy to be plugged into a custom dimension for 1.20.+ . I'd recommend having the atrocity it generates in a separate class and call it if necessary.

In the folder there is also an already created Climate list of the vanilla overworld generation as generated in https://misode.github.io/dimension/?version=1.20.3

WARNING: DYNAMICALLY GENERATING A DIMENSION AS RICH AS HEAVY IN ENTRIES AS THE VANILLA OVERWORLD VIA A DATA GENERATOR IS VERY VERY RESOURCE INTENSTIVE AND IS PROBABLY NOT WORTH IT! 
This script is design to work with whatever lengh any biomes json list is, but take that into account.

If instead you have a smaller json to convert (of no more than a couple hundred entries) you can make the conversion online [here](https://nullcharx.github.io/forge204utils/JSONToClimate)
