In order to use this, you need to setup the config first. I don't reccomend you read this in github as therer are formatting issues.
Example on how to use:

{

"token" : "2323",  -- This line is where you set your bot's token, easy enough I would say

"1" : 1221212121321,        -- the role "1221212121321" will be assigned if the user obtaines 1 invite
"5" : 2834734623625,        -- the role "2834734623625" will be assigned if the user obtaines 5 invites
"10": 8273232323232         -- the role "2834734623625" will be assigned if the user obtaines 10 invites

}

Keep in mind that you must chose your role basesd on the ID. You must go to Server Settings -> Roles -> Click on ... -> Copy ID.
You then paste that into the config.json file
