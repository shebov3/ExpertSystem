local inputController = {}
inputController.__index = inputController

--[[ Modules ]]
local Keys = require(script.nonRegisteredKeys)

--[[ Services ]]
local userInputService = game:GetService("UserInputService")

userInputService.InputBegan:Connect(function(input, gameProcessedEvent)
	
end)

userInputService.InputEnded:Connect(function(input, gameProcessedEvent)
	
end)

return inputController