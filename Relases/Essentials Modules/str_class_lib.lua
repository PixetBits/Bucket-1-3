function newStr(elin, lin, actS)

    -- str name[1] as[2] value[3] --
    vname = lin:sub(0, math.min(lin:find(' as ')) - 1)
    vvall = lin:sub(math.max(lin:find(' as ')) + 1)

    -- A other variable has the same name
    if actS[vname] ~= nil then sys.error(elin, 'c', "A other string variable has the same name of this.")
        
    -- If is a string --
    elseif isStr(vvall, actS) then
        
        -- Update value --
        if actS[vvall] ~= nil then vvall = actS[vvall] end
        
        -- Update variable --
        actS[vname] = vvall:gsub("'", '')

        -- Return string's table --
        return actS
    
    -- Wrong type --
    else sys.error(elin, 'c', "This is not a string value.") end
end

function isStr(vall, actS)

    -- Pure string --
    if vall:sub(1, 1) == "'" and vall:sub(-1) == "'" then return true

    -- Stored string --
    elseif actS[vall] ~= nil then return true
    
    -- Is not a string --
    else return false end
end