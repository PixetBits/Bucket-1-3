function newBol(elin, lin, actB)

    -- num name[1] as[2] value[3] --
    vname, vvall = sys.midle(lin, ' as ')

    -- A other variable has the same name
    if actB[vname] ~= nil then sys.error(elin, 'c', "Another bol variable has the same name of this.")

    -- If is a number --
    elseif isBol(vvall, actB) then
        
        -- Update value --
        if actB[vvall] ~= nil then vvall = actB[vvall] end
        
        -- Update variable --
        if vvall == 'yes' then actB[vname] = true end
        if vvall == 'not' then actB[vname] = false end

        -- Return bol's table --
        return actB
    
    -- Wrong type --
    else sys.error(elin, 'c', "This is not a boolean value.") end
end

function isBol(vall, actB)
    
    -- Pure bool --
    if vall == 'yes' or vall == 'not' then return true

    -- Stored bool --
    elseif actB[vall] ~= nil then return true
    
    -- Is not a bool --
    else return false end
end