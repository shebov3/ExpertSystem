local caret = {}
caret.__index = caret

--[[ Services ]]
local replicatedStorage = game:GetService("ReplicatedStorage")

--[[ Object Variables ]]
local label = replicatedStorage.Label

function caret.new(Frame:Frame)
	local self = setmetatable({}, caret)
	self.label = label:Clone()
	self.label.Text = "|"
	self.label.Parent = Frame
	self.label.ZIndex = 2
	return self
end

return caret