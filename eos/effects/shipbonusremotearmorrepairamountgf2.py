# shipBonusRemoteArmorRepairAmountGF2
#
# Used by:
# Variations of ship: Navitas (2 of 2)
type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"), "armorDamageAmount", src.getModifiedItemAttr("shipBonusGF2"), skill="Gallente Frigate")
