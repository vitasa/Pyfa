type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"), "maxRange", src.getModifiedItemAttr("shipBonusAC2"), skill="Amarr Cruiser")
