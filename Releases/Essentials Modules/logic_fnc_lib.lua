function door(elin, line, actN, actS, actB, actL)

    local keywords = {'equals', 'unlike', 'greater', 'smaller', 'amost+', 'amost-', 'and', 'or'}

    -- vall[0] ~~[1] vall[2] do: --

    -- Fix string space char --
    while line:match("%'(.+%s.+)%'") ~= nil do

        fidx, lidx = line:find("%'(.+)%'")

        line = line:gsub(line:sub(fidx, lidx), line:sub(fidx, lidx):gsub(' ', '{s}'))
    end

    -- Fix values --
    line = sys.split(line, ' ')

    -- Change all values for  --
    for word in pairs(line) do

        -- Values --

        -- Null value --
        if line[word] == 'nil' then line[word] = "'nil'"

        -- Is a number --
        elseif isNum(line[word], actN) then

            if actN[line[word]] ~= nil then line[word] = tostring(actN[line[word]]) end
        
        -- Is a string -- 
        elseif isStr(line[word], actS) then

            if actS[line[word]] ~= nil then line[word] = '\'' .. actS[line[word]]:gsub(' ', '{s}') .. '\'' end
        
        -- Is a bool --
        elseif isBol(line[word], actB) then

            if actB[line[word]] ~= nil then line[word] = actB[line[word]] end

            if line[word] == true or line[word] == 'yes' then line[word] = 'true' end
            if line[word] == false or line[word] == 'not' then line[word] = 'false' end

        -- Is a list --
        elseif isLst(line[word], actL) then

            if actL[line[word]] ~= nil then line[word] = '%[' .. sys.tabletostr(actL[line[word]]) .. '%]'
            else line[word] = '%[' .. line[word] .. '%]' end
        
        -- Is a keyword --
        elseif sys.finds(keywords, line[word]) == nil then
            
            sys.error(elin, 'c', 'Strange value in logic statlement.')
        end
    end

    -- Join again --
    line = sys.tabletostr(line):gsub(',', '')

    -- Equals --
    while line:find(' equals ') ~= nil do

        -- Get words around keyword --
        farg, larg = sys.midle(line, ' equals ')

        -- If finds it --
        if farg ~= nil and larg ~= nil then

            -- Get entire line to replace --
            subs = farg .. ' equals ' .. larg

            -- Replace by boolean value --
            if line == subs then line = tostring(farg == larg)
            else line = line:gsub(subs, tostring(farg == larg)) end
        end
    end

    -- Unlike --
    while line:find(' unlike ') ~= nil do
        
        -- Get words around keyword --
        farg, larg = sys.midle(line, ' unlike ')

        -- If finds it --
        if farg ~= nil and larg ~= nil then

            -- Get entire line to replace --
            subs = farg .. ' unlike ' .. larg

            -- Replace by boolean value --
            line = line:gsub(subs, tostring(farg ~= larg))
        end
    end

    -- Greater --
    while line:find(' greater ') ~= nil do
        
        -- Get words around keyword --
        farg, larg = sys.midle(line, ' greater ')

        -- If finds it --
        if tonumber(farg) ~= nil and tonumber(larg) ~= nil then
    
            -- Get entire line to replace --
            splt = sys.split(line, ' greater ')
            subs = farg .. ' greater ' .. larg

            -- Replace by boolean value --
            line = line:gsub(subs, tostring(tonumber(farg) > tonumber(larg)))
        
        -- Not numbers --
        elseif farg ~= nil and larg ~= nil then sys.error(elin, 'c', 'Bucket cannot compare non numeric values.') end
    end

    -- Smaller --
    while line:find(' smaller ') ~= nil do
        
        -- Get words around keyword --
        farg, larg = sys.midle(line, ' smaller ')

        -- If finds it --
        if tonumber(farg) ~= nil and tonumber(larg) ~= nil then
    
            -- Get entire line to replace --
            splt = sys.split(line, ' smaller ')
            subs = farg .. ' smaller ' .. larg

            -- Replace by boolean value --
            line = line:gsub(subs, tostring(tonumber(farg) < tonumber(larg)))
        
        -- Not numbers --
        elseif farg ~= nil and larg ~= nil then sys.error(elin, 'c', 'Bucket cannot compare non numeric values.') end
    end

    -- And --
    while line:find(' and ') ~= nil do

        -- Get words around keyword --
        farg, larg = sys.midle(line, ' and ')

        -- If finds it --
        if farg ~= nil and larg ~= nil then
    
            -- Get entire line to replace --
            splt = sys.split(line, ' and ')
            subs = farg .. ' and ' .. larg

            -- Convert to default boolean --
            if farg == 'true' then farg = true end
            if farg == 'false' then farg = false end

            if larg == 'true' then larg = true end
            if larg == 'false' then larg = false end

            -- Replace by boolean value --
            line = line:gsub(subs, tostring(farg and larg))
        end
    end

    -- Or --
    while line:find(' or ') ~= nil do

        -- Get words around keyword --
        farg, larg = sys.midle(line, ' or ')

        -- If finds it --
        if farg ~= nil and larg ~= nil then
    
            -- Get entire line to replace --
            splt = sys.split(line, ' or ')
            subs = farg .. ' or ' .. larg

            -- Convert to default boolean --
            if farg == 'true' then farg = true end
            if farg == 'false' then farg = false end

            if larg == 'true' then larg = true end
            if larg == 'false' then larg = false end

            -- Replace by boolean value --
            line = line:gsub(subs, tostring(farg or larg))
        end
    end

    if line == 'true' then return true
    elseif line == 'false' then return false
    else sys.error(elin, 'c', 'This is not a boolean statlement.') end
end