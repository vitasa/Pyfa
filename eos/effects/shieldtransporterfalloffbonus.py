type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Shield Booster", "falloffEffectiveness", src.getModifiedItemAttr("falloffBonus"))
