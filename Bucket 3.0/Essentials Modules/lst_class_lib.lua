function newLst(elin, line, actL)

    -- lst[type] name as value --

    -- Fix sintax --
    if line:find('%s*%]%s*') ~= nil then line = line:gsub('%s*%]%s*', '%]') end
    if line:find('%s*%:%s*') ~= nil then line = line:gsub('%s*%:%s*', '%:') end
    if line:find('%s*%,%s*') ~= nil then line = line:gsub('%s*%,%s*', '%,') end

    -- Get list type --
    ltype = line:sub(1, 5)
    ltype = ltype:sub(2, -2)

    line = line:sub(6)

    -- Get name and value --
    vname, vvall = sys.midle(line:gsub(' ', '{s}'):gsub('{s}as{s}', ' as '), ' as ')
    vvall = vvall:gsub('{s}', ' ')

    -- A other variable has the same name --
    if actL[vname] ~= nil then sys.error(elin, 'c', "Another lst variable has the same name of this.")

    -- If is a list --
    elseif isLst(vvall, actL) then
        
        list = {}
        list.type = ltype

        -- Remove square brackets --
        vvall = vvall:sub(2, -2)

        -- Multiple values --
        if vvall:find(',') ~= nil then
            
            -- Split --
            item = sys.split(vvall, ',')

            -- Do it for all items --
            for itm in pairs(item) do

                -- Get index and value --
                subs = sys.split(item[itm], ':')
                indx = subs[1]
                vall = subs[2]

                -- A number list --
                if ltype == 'num' then
                
                    if tonumber(vall) ~= nil then list[indx] = tonumber(vall)
                    else sys.error('A value in this list does not match the list type.') end

                -- A string list --
                elseif ltype == 'str' then
                
                    if vall:find("^%'.*%'") then list[indx] = vall:gsub('\'', '')
                    else sys.error('A value in this list does not match the list type.') end
                
                -- A bool list --
                elseif ltype == 'bol' then
                
                    if vall == 'yes' or vall == 'not' then
                        
                        if vall == 'yes' then list[indx] = true end
                        if vall == 'not' then list[indx] = false end

                    else sys.error('A value in this list does not match the list type.') end
                
                -- A variable or a strange vallue --
                else sys.error(elin, 'c', 'You cannot assign a variable, or non default data type, as start value.') end
            end

            -- Store list --
            actL[vname] = list
        
        -- Single value --
        elseif vvall ~= '[:]' then
            
            -- Get index and value --
            indx, vall = sys.midle(item[itm], ':')

            -- A number list --
            if ltype == 'num' then
                
                if tonumber(vall) ~= nil then list[indx] = tonumber
                else sys.error('A value in this list does not match the list type.') end

            -- A string list --
            elseif ltype == 'str' then
            
                if vall:find("^%'.*%'") then list[indx] = vall:gsub('\'', '')
                else sys.error('A value in this list does not match the list type.') end
            
            -- A bool list --
            elseif ltype == 'bol' then
            
                if vall == 'yes' or vall == 'not' then
                    
                    if vall == 'yes' then list[indx] = true end
                    if vall == 'not' then list[indx] = false end

                else sys.error('A value in this list does not match the list type.') end
            
            -- A variable or a strange vallue --
            else sys.error('You cannot assign a variable, or non default data type, as start value.') end

            -- Store list --
            actL[vname] = list
        
        -- Empty list --
        elseif vvall == '[:]' then actL[vname] = list end
    
    -- This is not a list --
    else sys.error(elin, 'c', "This is not a list value.") end

    return actL
end

function isLst(vall, actL)
    
    -- String lst --
    if vall:gsub(' ', '{s}'):match('(.+)%:(.+)') then return true

    -- Stored lst --
    elseif actL[vall] ~= nil then return true
    
    -- Is not a lst --
    else return false end
end