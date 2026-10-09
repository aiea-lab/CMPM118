% FACTS 

% format: house_member(character, house).
house_member(harry, gryffindor).
house_member(hermione, gryffindor).
house_member(draco, slytherin).
house_member(cedric, hufflepuff).

% format: wand_core(character, core_material).
wand_core(harry, phoenix_feather).
wand_core(hermione, dragon_heartstring).
wand_core(draco, unicorn_hair).

% format: parent_status(character, mother_type, father_type).
parent_status(harry, muggleborn, pureblood).
parent_status(hermione, muggle, muggle).
parent_status(draco, pureblood, pureblood).
parent_status(ron, pureblood, pureblood).

% RULES 

% Rule 1: 
character_trait(Character, brave) :- house_member(Character, gryffindor).
character_trait(Character, cunning) :- house_member(Character, slytherin).
character_trait(Character, loyal) :- house_member(Character, hufflepuff).

% Rule 2: 
blood_status(Character, pureblood) :- parent_status(Character, pureblood, pureblood).
blood_status(Character, muggleborn) :- parent_status(Character, muggle, muggle).
blood_status(Character, halfblood) :- parent_status(Character, Mother, Father), Mother \= Father.
