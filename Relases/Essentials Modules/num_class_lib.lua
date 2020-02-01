function newNum(elin, lin, actN)

    -- num name[1] as[2] value[3] --
    vname, vvall = sys.midle(lin, ' as ')

    -- A other variable has the same name
    if actN[vname] ~= nil then sys.error(elin, 'c', "Another num variable has the same name of this.")

    -- If is a number --
    elseif isNum(vvall, actN) then
        
        -- Update value --
        if actN[vvall] ~= nil then vvall = actN[vvall] end
        
        -- Update variable --
        actN[vname] = tonumber(vvall)

        -- Return num's table --
        return actN
    
    -- Wrong type --
    else sys.error(elin, 'c', "This is not a numeric value.") end
end

function isNum(vall, actN)

    -- Pure num --
    if type(vall) == 'number' then return true
    
    -- String number --
    elseif tonumber(vall) ~= nil then return true

    -- Stored num --
    elseif actN[vall] ~= nil then return true
    
    -- Is not a num --
    else return false end
end

function make(elin, vname, ovall, signl, actV)

    -- Get variable value --
    vvall = actV[vname]

    -- Sum --
    if signl == '+' then

        if actV.type == 'num' then

            if type(ovall) == 'number' then actV[vname] = vvall + ovall
            else sys.error(elin, 'c', "Cannot make a operation between number and string.") end
        end

        if actV.type == 'str' then
            
            if type(ovall) == 'string' then actV[vname] = vvall .. ovall
            else sys.error(elin, 'c', "Cannot sum a string with a non string value.") end
        end
    end

    -- sub --
    if signl == '-' then
        
        if actV.type == 'num' then

            if type(ovall) == 'number' then actV[vname] = vvall - ovall
            else sys.error(elin, 'c', "Cannot make a operation between number and string.") end
        end

        if actV.type == 'str' then
            
            if type(ovall) == 'string' then actV[vname] = string.gsub(vvall, ovall, '')
            else sys.error(elin, 'c', "Cannot remove from a string a non string value.") end
        end
    end

    -- mul --
    if signl == '*' then
        
        if actV.type == 'num' then

            -- To check if is an float --
            if type(ovall) == 'number' then actV[vname] = vvall * ovall
            else sys.error(elin, 'c', "Cannot make a operation between number and string.") end
        end

        if actV.type == 'str' then
            
            if type(ovall) == 'number' then
                
                num, brk = math.modf(ovall)
                
                -- Have no broken numbers --
                if brk == 0 then actV[vname] = string.rep(vvall, ovall)
                else sys.error(elin, 'c', "Cannot multiply a string by non integer number.") end

            else sys.error(elin, 'c', "Cannot multiply a string by a non numeric value.") end
        end
    end

    -- div --
    if signl == '/' then
        
        if actV.type == 'num' then

            -- To check if is an float --
            if type(ovall) == 'number' then actV[vname] = vvall / ovall
            else sys.error(elin, 'c', "Cannot make a operation between number and string.") end
        end

        if actV.type == 'str' then sys.error(elin, 'c', "Cannot divide a string.") end
    end

    -- div --
    if signl == '^' then
        
        if actV.type == 'num' then

            -- To check if is an float --
            if type(ovall) == 'number' then actV[vname] = math.pow(vvall, ovall)
            else sys.error(elin, 'c', "Cannot make a operation between number and string.") end
        end

        if actV.type == 'str' then sys.error(elin, 'c', "Cannot square a string.") end
    end

    -- div --
    if signl == '%' then
        
        if actV.type == 'num' then

            -- To check if is an float --
            if type(ovall) == 'number' then actV[vname] = vvall % ovall
            else sys.error(elin, 'c', "Cannot make a operation between number and string.") end
        end

        if actV.type == 'str' then sys.error(elin, 'c', "Cannot divide a string.") end
    end

    -- Return vall's table --
    return actV
end