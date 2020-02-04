to = {}

function to.math(elin, line, actN)

    -- Sin --
    if line:match('math_sin%:(.+)') then

        fidx, lidx = line:find('math_sin:(.+)')
        vall = line:sub(fidx + 9, lidx)

        if isNum(vall, actN) == true then
            
            if actN[vall] ~= nil then vall = actN[vall]
            else vall = tonumber(vall) end
        
        else sys.error(elin, 'c', 'Unknow numeric variable.') end

        line = line:gsub(line:sub(fidx, lidx), tostring(math.sin(vall)):sub(1, 6))
    end

    -- Cos --
    if line:match('math_cos%:(.+)') then

        fidx, lidx = line:find('math_cos:(.+)')
        vall = line:sub(fidx + 9, lidx)

        if isNum(vall, actN) == true then
            
            if actN[vall] ~= nil then vall = actN[vall]
            else vall = tonumber(vall) end
        
        else sys.error(elin, 'c', 'Unknow numeric variable.') end

        line = line:gsub(line:sub(fidx, lidx), tostring(math.cos(vall)):sub(1, 6))
    end

    -- Tan --
    if line:match('math_tan%:(.+)') then

        fidx, lidx = line:find('math_tan:(.+)')
        vall = line:sub(fidx + 9, lidx)

        if isNum(vall, actN) == true then
            
            if actN[vall] ~= nil then vall = actN[vall]
            else vall = tonumber(vall) end
        
        else sys.error(elin, 'c', 'Unknow numeric variable.') end

        line = line:gsub(line:sub(fidx, lidx), tostring(math.tan(vall)):sub(1, 6))
    end

    -- Rand --
    if line:match('math_ran%:(.+),(%s?)(.+)') then

        fidx, lidx = line:find('math_ran:(.+)')
        vall = line:sub(fidx + 9, lidx)

        -- Fix spaces --
        vall = vall:gsub(', ', ',')
        vall = vall:gsub(' ,', ',')
        vall = sys.split(vall, ',')

        farg, larg = vall[1], vall[2]

        -- Get value of firt argument --
        if isNum(farg, actN) == true then
            
            if actN[farg] ~= nil then farg = actN[farg]
            else farg = tonumber(farg) end
        
        else sys.error(elin, 'c', 'Unknow numeric variable (1st argument).') end

        -- Get value of last argument --
        if isNum(larg, actN) == true then
            
            if actN[larg] ~= nil then larg = actN[larg]
            else larg = tonumber(larg) end
        
        else sys.error(elin, 'c', 'Unknow numeric variable (2th argument).') end

        -- Set random seed --
        math.randomseed(os.time())

        rand = math.random(farg, larg)
        line = line:gsub(line:sub(fidx, lidx), tostring(rand))
    end
    
    return line
end

return to