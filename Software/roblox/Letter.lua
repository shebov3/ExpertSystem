local letter = {}
letter.__index = letter

--[[ Services ]]
local replicatedStorage = game:GetService("ReplicatedStorage")

--[[ Object Variables ]]
local label = replicatedStorage.Label

function letter.new()
    local self = setmetatable({}, letter)
    self.label = label:Clone()
    self.
end

return letter