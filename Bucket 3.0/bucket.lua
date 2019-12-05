-- My own library --
require('Essentials Modules/SystemLib')
require('Essentials Modules/RunnerLib')

-- Open and store script --
local data = {}

function loadfile(name)

    -- Fix extention --
    if string.sub(name, -3) ~= ".bk" then
        
        name = name .. ".bk"
    end
    
    -- This file does not exists --
    if io.open(name) == nil then
        
        sys.error('', '', "This file does not exist. Please check the name and try again.")
    end

    bkfile = {}
    script = {}
    
    -- Multyple comands in a single line --
    for line in io.lines(name) do
        
        -- Semicolon --
        if line:find(';') ~= nil then
            
            if line:find('; ') ~= nil then line = line:gsub('; ', ';') end
            split = sys.split(line, ';')

            table.insert(script, split[1])
            split[1] = nil

            for sub in pairs(split) do

                table.insert(script, split[sub])
            end
        
        else table.insert(script, line) end
    end

    -- Read every line --
    for line in pairs(script) do

        line = script[line]

        -- Remove comments --
        if string.find(line, '--') ~= nil then

            -- Remove comment --
            line = string.gsub(line, '%-%-(.-)%-%-', '')
        end

        -- Remove tabs --
        line = string.gsub(line, '\t', '')
        
        -- Remove double spaces --
        line = string.gsub(line, '%s%s+', ' ')
        line = string.gsub(line, '\t', '')

        -- First char is a space --
        while string.sub(line, 1, 1) == " " do
            
            line = string.sub(line, 2)
        end

        -- Break line in words --
        local word = sys.split(line, ' ')
        local stkd = word[1]

        -- Put it together again --
        for w = 2, #word do
        
            stkd = stkd .. " " .. word[w]
        end

        -- Update value --
        line = stkd

        -- Don't store blank lines --
        if line ~= "" then data[#data + 1] = line end
    end

    -- Fix name --
    while name:find('\\') ~= nil do
        
        index = name:find('\\')
        name = name:sub(index + 1)
    end

    name = name:gsub('.bk', '')

    io.write("\nRuning: " .. name .. '...\n')
    io.write(string.rep('=', string.len('Runing: ' .. name .. '...')) .. '\n\n')

    -- Call runner --
    run(data, 1, true, name)

    io.write('\n\n=======================\n')
    io.write("Type any key to exit...\n")
    io.read()
end

-- Argument --
if arg[1] ~= nil then
    
    input = arg[1]

-- File name --
else

    -- Copyright (c) --
print('\nBucket by BinaryBrain_ [version: 3.0.0]\nCopyright(c) 2019 Mateus Morais (mateusmoraisdias3@gmail.com).\nAll rights reserved.\n')

    io.write("Script name: ")
    input = io.read()
end

loadfile(input)