-- Expecifield libraries --
require('Essentials Modules/num_class_lib')
require('Essentials Modules/str_class_lib')
require('Essentials Modules/bol_class_lib')
require('Essentials Modules/lst_class_lib')
require('Essentials Modules/logic_fnc_lib')

-- Imported libs --
local ilib = {}

-- Tasks --
local actT = {}

-- Variables storange --
local actN = {}
actN.type = "num"

local actS = {}
actS.type = "str"

local actB = {}
actB.type = "bol"

local actL = {}
actL.type = "lst"

-- Class management --
local oncl = false

-- Function manangement --
local onfc = false
local ontk = false
local askd = false

-- If-Even-Else stuff --
local ifs = {}

ifs.index = 0
ifs.lblck = {}
ifs.stats = {}

-- While Loop stuff --
local lop = {}

lop.condt = {}
lop.on_sb = {}
lop.index = 0

function run(lines, clin, enbd, name, sub)

    -- Univesal breaker --
    local brk = false

    local line = lines[clin]
    local elin = line

    -- Error skip --
    if line:sub(-1) == '?' then line = line:sub(0, -2) end

--# Class stuff --------------------------------------------#--

    -- Main lib --
    if lines[1] ~= "[to Basic]" then sys.error('', 's', 'Main class "[to Basic]" was not imported.') end

    -- Import lib --
    if line:sub(1, 3) == "[to" and line:sub(-1) == "]" and line ~= "[to Basic]" then

        -- The file exists --
        if io.open('Importable Libraries/' .. line .. '_lib.lua') == nil then sys.error(elin, 'c', 'This library could not be found.')
        else ilib[line] = require('Importable Libraries/' .. line .. '_lib') end
    end

    -- Enter and exit of class --
    if line:sub(1, 1) == "#" then
        
        mln = sys.split(line, ' ')
        
        -- #name in Bucket: --

        -- Other class
        if oncl then sys.error(elin, 'c', 'Ambiguity in the class declaration.') end

        if mln[1]:lower() ~= "#" .. name:lower() then sys.error(line, 's', 'The class name must be the same of file.') end
        if mln[2] ~= "in" then sys.error(line, 's', 'Missing keyword "in".') end
        if mln[3] ~= "Bucket:" then sys.error(line, 's', 'Missing keyword "Bucket:".') end

        oncl = true
    end

--# Open-close keywords ------------------------------------#--

    -- Enter in main func --
    if line:sub(-5) == "open:" then
        
        onfc = true
        enbd = true
    end

    -- Exit from main func --
    if line == "end m." then

        onfc = false
        enbd = false
    end
    
    -- Enter in task --
    if line:find('task:') ~= nil then 
        
        if not oncl then sys.error(elin, 's', 'Task out of class block.')
        elseif onfc then sys.error(elin, 's', 'Attempt to declare a task inside the main block.')
        else
            
            ontk = true

            -- Don't run tasks --
            enbd = false
        end
    end

    -- Exit from task --
    if line == "end t." then
        
        if ontk then

            ontk = false
            enbd = true
        
        else sys.error(elin, 's', 'Attempt to close a closed task.') end
    end

    -- Exit of if-even-else block --
    if line == "end." then

        enbd = true
        ifs.index = ifs.index - 1
    end

    -- Exit from loop --
    if line == "end l." then enbd = true end

--# Task stuff ---------------------------------------------#--

    -- Find all tasks --
    if not askd then
        
        local cname = ''

        -- Run all lines --
        for indx in pairs(lines) do
            
            lin = lines[indx]

            -- Declaration of task --
            if lin:find('task:') ~= nil then

                ontk = true

                if not lin:match('.+task:.*') then sys.error(lin, 's', 'Task syntax is wrong') end

                -- Fix syntax --
                if lin:find(':') ~= nil then
                    
                    if lin:find(': ') ~= nil then lin = lin:gub(': ', ':') end
                    if lin:find(' :') ~= nil then lin = lin:gub(' :', ':') end
                end

                -- name task:arg --
                word = sys.split(lin, ' ')

                cname = word[1]

                -- Argument --
                if word[2]:sub(-1) ~= ":" then arg = sys.split(word[2], ':')[2] end

                actT[cname] = {}

                -- Store values --
                actT[cname].flin = indx

                -- Store argument --
                actT[cname].arg = arg
            end

            -- End of task block --
            if lin:find('end t.') ~= nil then
                
                if not ontk then sys.error(lin, 's', 'No task block to close.')
                else ontk = false end
                
                actT[cname].llin = indx
            end
        end

        -- Do it once --
        askd = true
    end

--# Script functions and resourses -------------------------#--

    -- Run lines on main --
    if enbd and onfc and oncl then
    --# Put yours lib's modules below ----------------------#--

        -- to Mathf's module --
        if ilib['[to Mathf]'] then
            
            line = ilib['[to Mathf]'].math(elin, line, actN)
        end

    --# Replaceable values ---------------------------------#--

        -- Input --
        if line:find(' sand ') ~= nil then

            -- Argment in sand --
            if string.find(line, ' with ') ~= nil then
                
                mln = string.sub(line, math.min(string.find(line, ' with ')))
                arg = mln:gsub(' with ', '')

                -- Update argment --
                if isStr(arg, actS) then
                    
                    if actS[arg] ~= nil then arg = actS[arg]
                    else arg = arg:gsub("'", '') end
                
                -- This argment isn't a string -- 
                else sys.error(elin, 'c', 'This is not a string.') end

                -- Special chars --
                if arg:find('{s}') ~= nil then arg = arg:gsub('{s}', ' ') end
                if arg:find('{q}') ~= nil then arg = arg:gsub('{q}', '\'') end
                if arg:find('{n}') ~= nil then arg = arg:gsub('{n}', '\n') end
                if arg:find('{t}') ~= nil then arg = arg:gsub('{t}', '\t') end

                io.write(arg)
            end

            input = io.read()
            line = line:gsub(line:sub(math.min(line:find('sand '))), "'" .. input .. "'")
        end

        -- Lst size --
        if line:find('size:') ~= nil then
            
            -- String indexes --
            fidx, lidx = line:find('size:')
            lidx = line:find(' ', lidx)

            mln = line:sub(fidx, lidx)
            val = sys.split(mln, ':')

            if actL[val[2]] ~= nil then line = line:gsub(mln, tostring(sys.length(actL[val[2]]) - 1))
            else sys.error(elin, 'c', "Unknow list value.") end
        end

    --# If-even-else system --------------------------------#--

        -- If Block --
        if line:sub(1, 3) == "if " then

            -- Enter into next block --
            ifs.index = ifs.index + 1

            -- do: --
            if line:find(' do:') ~= nil and line:sub(-4) == " do:" then line = line:gsub(' do:', '')
            else sys.error(elin, 's', 'Missing keyword "do:".') end

            -- True or false? --
            ifs.stats[ifs.index] = door(elin, line:sub(4), actN, actS, actB, actL)

            -- Enable next lines --
            if ifs.stats[ifs.index] == true then enbd = true
            else enbd = false end

            -- Set last logic block --
            ifs.lblck[ifs.index] = "if"
        end

        -- Maybe Block --
        if line:sub(1, 5) == "even " then

            -- Enter into next block --
            ifs.index = ifs.index + 1

            -- do: --
            if line:find(' do:') ~= nil and line:sub(-4) == " do:" then line = line:gsub(" do:", '')
            else sys.error(elin, 's', 'Missing keyword "do:".') end

            -- The last block must be 'if' or 'even' --
            if ifs.lblck[ifs.index] == "if" or ifs.lblck[ifs.index] == "even" then

                -- If last block was false do: --
                if ifs.stats[ifs.index] == false then

                    -- True or false? --
                    ifs.stats[ifs.index] = door(elin, line:sub(6), actN, actS, actB, actL)

                    -- Enable next lines --
                    if ifs.stats[ifs.index] == true then enbd = true
                    else enbd = false end

                    -- Set last logic block --
                    ifs.lblck[ifs.index] = "even"
                
                -- Disable lines --
                else enbd = false end
            
            -- It's not --
            else sys.error(elin, 's', 'Maybe Block must be after "if" block.') end
        end

        -- Else Block --
        if line == "else:" then

            -- Enter into next block --
            ifs.index = ifs.index + 1

            -- The last block must be 'if' or 'even' --
            if ifs.lblck[ifs.index] == "if" or ifs.lblck[ifs.index] == "even" then

                -- Enable next lines --
                if ifs.stats[ifs.index] == false then enbd = true
                else enbd = false end

                -- Set last logic block --
                ifs.lblck[ifs.index] = "else"

            -- It's not --
            else sys.error(elin, 's', 'Else Block must be after "if" or "even" block.') end
        end

    --# Non user dependent functions -----------------------#--

        -- New variables --
        if line:sub(1, 4) == "num " then actN = newNum(elin, line:sub(5), actN) end
        if line:sub(1, 4) == "str " then actS = newStr(elin, line:sub(5), actS) end
        if line:sub(1, 4) == "bol " then actB = newBol(elin, line:sub(5), actB) end

        if line:sub(1, 3) == "lst" then actL = newLst(elin, line:gsub('(lst)%s*', ''), actL) end

        -- Bucket output --
        if line:sub(1, 6) == "show: " then

            -- Insert var --
            if line:find('%[%d%]') ~= nil then

                if not line:find(' with ') then sys.error(elin, 's', 'Missing keyword "with".') end

                -- Get variables --
                arg = line:sub(math.max(line:find(' with ')) + 1)
                arg = arg:gsub(' ', '')

                -- Remove this of line --
                line = line:gsub(line:sub(math.min(line:find(' with '))), '')

                -- Split in ',' --
                if string.find(arg, ',') ~= nil then arg = sys.split(arg, ',') end

                -- Replace every ocurrange --
                if type(arg) == 'table' then

                    local index = 0

                    for a in pairs(arg) do
                
                        -- Update value --

                        -- Number --
                        if actN[arg[a]] ~= nil then
                            
                            -- Replace value --
                            line = line:gsub('%[' .. tostring(index) .. '%]', tostring(actN[arg[a]]))
                        
                        -- String --
                        elseif actS[arg[a]] ~= nil then
                            
                            -- Replace value --
                            line = line:gsub('%[' .. tostring(index) .. '%]', actS[arg[a]])

                        -- Bool --
                        elseif actB[arg[a]] ~= nil then

                            -- Fix nomenclature --
                            if actB[arg[a]] == true then line = line:gsub('%[' .. tostring(index) .. '%]', 'yes')
                            else line = line:gsub('%[' .. tostring(index) .. '%]', 'not') end
                        
                        -- List --
                        elseif actL[arg[a]] ~= nil then

                            -- Remove list type value --
                            recover = actL[arg[a]].type
                            actL[arg[a]].type = nil

                            -- Replace value --
                            line = line:gsub('%[' .. tostring(index) .. '%]', sys.tabletostr(this))
                            actL[arg[a]].type = recover
                        
                        -- No stored value --
                        else

                            -- Replace value --
                            line = line:gsub('%[' .. tostring(index) .. '%]', arg[a])
                        end

                        index = index + 1
                    end
                 
                -- Replace once --
                elseif arg ~= nil then
                    
                    -- Update value --

                    -- Num --
                    if actN[arg] ~= nil then val = tostring(actN[arg])
                    
                    -- String --
                    elseif actS[arg] ~= nil then val = actS[arg]

                    -- Bool --
                    elseif actB[arg] ~= nil then
                        
                        val = actB[arg]

                        -- Fix nomenclature --
                        if val == true then val = 'yes' end
                        if val == false then val = 'not' end
                    
                    -- List --
                    elseif actL[arg] ~= nil then
                        
                        -- Remove list type value --
                        recover = actL[arg].type
                        actL[arg].type = nil

                        val = sys.tabletostr(actL[arg])
                        actL[arg].type = recover
                    
                    -- Non existent variable --
                    else sys.error(elin, 'c', 'Unknow variable.') end

                    line = line:gsub('%[0%]', val)
        
                -- Without argment --
                else sys.error(elin, 's', 'There is no argment to print.') end
            end

            -- Remove prefix --
            mln = line:gsub('show: ', '')

            -- Special chars --
            if mln:find('{s}') ~= nil then mln = mln:gsub('{s}', ' ') end
            if mln:find('{q}') ~= nil then mln = mln:gsub('{q}', '\'') end
            if mln:find('{n}') ~= nil then mln = mln:gsub('{n}', '\n') end
            if mln:find('{b}') ~= nil then mln = mln:gsub('{b}', '\b') end
            if mln:find('{t}') ~= nil then mln = mln:gsub('{t}', '\t') end

            -- Is a string --
            if isStr(mln, actS) then

                if actS[mln] ~= nil then
                    
                    mln = actS[mln]

                    -- Fix special characters --
                    if mln:find('{s}') ~= nil then mln = mln:gsub('{s}', ' ') end
                    if mln:find('{q}') ~= nil then mln = mln:gsub('{q}', '\'') end
                    if mln:find('{n}') ~= nil then mln = mln:gsub('{n}', '\n') end
                    if mln:find('{b}') ~= nil then mln = mln:gsub('{b}', '\b') end
                    if mln:find('{t}') ~= nil then mln = mln:gsub('{t}', '\t') end
                    
                    -- Show it --
                    io.write(mln)

                else
                    
                    mln = string.sub(mln, 2, -2)
                    io.write(mln)
                end
            
            -- Wrong argment --
            else sys.error(elin, 'c', 'Bucket cannot show this.') end
        end

        -- Value manipulation --
        
        -- Set --
        if line:sub(1, 5) == "set: " then
            
            -- Remove keyword --
            mln = line:gsub('set: ', '')

            -- Split it --
            split = sys.split(mln, ' to ')
            var = split[1]
            val = split[2]

            -- Set a num variable --
            if actN[var] ~= nil then
                
                -- The value to asign is of the same type --
                if isNum(val, actN) then
                    
                    if actN[val] ~= nil then actN[var] = actN[val]
                    else actN[var] = tonumber(val) end
                
                else sys.error(elin, 'c', 'Unknow value.') end
            
            -- Set a str variable --
            elseif actS[var] ~= nil then
                
                -- The value to asign is of the same type --
                if isStr(val, actS) then
                    
                    if actS[val] ~= nil then actS[var] = actS[val]
                    else actS[var] = val:gsub('\'', '') end
                
                else sys.error(elin, 'c', 'Unknow value.') end

             -- Set a bol variable --
            elseif actB[var] ~= nil then
                
                -- The value to asign is of the same type --
                if isBol(val, actB) then
                    
                    if actB[val] ~= nil then actB[var] = actB[val]
                    else
                        if val == 'yes' then actB[var] = true
                        else actB[var] = false end
                    end
                
                else sys.error(elin, 'c', 'Unknow value.') end
            
            -- Unknow variable --
            else sys.error(elin, 'c', 'This variable does not exist.') end
        end

        -- Both --
        if line:sub(1, 6) == "both: " then
            
            -- Remove keyword --
            mln = line:gsub('both: ', '')

            -- x, y .. z as vall --
            if mln:find(', ') then mln = mln:gsub(', ', ',') end
            var, val = sys.midle(mln, ' as ')

            -- Get all variables --
            var = sys.split(var, ',')

            -- No values splited --
            if var == nil then sys.error(elin, 's', 'You have just one or less variables.') end
            
            -- Check first value type --
            if actN[var[1]] ~= nil then ftyp = 'num' end
            if actS[var[1]] ~= nil then ftyp = 'str' end
            if actB[var[1]] ~= nil then ftyp = 'bol' end

            -- Assign value to all variables --
            for item in pairs(var) do
                
                -- All are a number --
                if ftyp == 'num' then
                    
                    -- The variable is a number --
                    if actN[var[item]] ~= nil then

                        if isNum(val, actN) then actN[var[item]] = tonumber(val)
                        else sys.error(elin, 'c', 'This value is not of the same type of your variables.') end
                    
                    else sys.error(elin, 'c', 'This variable is not a number.') end
                end

                -- All are a string --
                if ftyp == 'str' then
                    
                    -- The variable is a string --
                    if actS[var[item]] ~= nil then

                        if isStr(val, actS) then actS[var[item]] = val:gsub('\'', '')
                        else sys.error(elin, 'c', 'This value is not of the same type of your variables.') end
                    
                    else sys.error(elin, 'c', 'This variable is not a string.') end
                end

                -- All are a bool --
                if ftyp == 'bol' then
                    
                    -- The variable is a bool --
                    if actB[var[item]] ~= nil then

                        if isBol(val, actB) then
                            
                            if val == 'yes' then actB[var[item]] = true end
                            if val == 'not' then actB[var[item]] = false end

                        else sys.error(elin, 'c', 'This value is not of the same type of your variables.') end
                    
                    else sys.error(elin, 'c', 'This variable is not a bool.') end
                end
            end
        end

        -- Convert --
        if line:sub(1, 9) == "convert: " then

            -- Remove keyword --
            mln = line:gsub('convert: ', '')

            -- convert var[1] to[2] type[3] --
            
            -- Get values --
            if mln:find(' to ') ~= nil then

                vname, ntype = sys.midle(mln, ' to ')

            else sys.error(elin, 's', 'Missing keyword "to".') end

            -- Convert to num --
            if ntype == 'num' then

                -- A Str --
                if isStr(vname, actS) then

                    -- Update value --
                    if actS[vname] ~= nil then vvall = actS[vname]
                    else sys.error(elin, 'c', 'Unable to convert a nonexistent variable.') end

                    -- Is not a num --
                    if actN[vname] == nil then

                        if tonumber(vvall) ~= nil then actN[vname] = tonumber(vvall)
                        else sys.error(elin, 'c', 'Bucket cannot convert this non numeric value.') end

                        actS[vname] = nil

                    else sys.error(elin, 'c', 'You already have a num with the same name.') end
                end

                -- A bol --
                if isBol(vname, actB) then

                    -- Update value --
                    if actB[vname] ~= nil then vvall = actB[vname] end

                    if actN[vname] == nil then
                        
                        if vvall == true then actS[vname] = 1 end
                        if vvall == false then actS[vname] = 0 end

                        actB[vname] = nil

                    else sys.error(elin, 'c', 'You already have a num with the same name.') end
                end

            -- Convert to string --
            elseif ntype == 'str' then

                -- A num --
                if isNum(vvall, actN) then

                    -- Update value --
                    if actN[vname] ~= nil then vvall = actN[vname]
                    else sys.error(elin, 'c', 'Unable to convert a nonexistent variable.') end

                    if actS[vname] == nil then actS[vname] = tostring(vvall)
                    else sys.error(elin, 'c', 'You already have a string with the same name.') end

                    actN[vname] = nil
                end

                -- A bol --
                if isBol(vvall, actB) then

                    -- Update value --
                    if actB[vname] ~= nil then vvall = actB[vname] end

                    if actS[vname] == nil then
                        
                        if vvall == true then actS[vname] = 'yes' end
                        if vvall == false then actS[vname] = 'not' end

                        actB[vname] = nil

                    else sys.error(elin, 'c', "You already have a string with the same name.") end
                end

            -- Convert to bool --
            elseif ntype == 'bol' then

                -- A int --
                if isNum(vname, actN) then

                    -- Update value --
                    if actN[vname] ~= nil then vvall = actN[vname]
                    else sys.error(elin, 'c', 'Unable to convert a nonexistent variable.') end

                    if actB[vname] == nil then
                        
                        if vvall == 0 then actB[vname] = false
                        else actB[vname] = true end

                        actN[vname] = nil

                    else sys.error(elin, 'c', 'You already have a bool with the same name.') end
                end

                -- A string --
                if isStr(vname, actS) then

                    -- Update value --
                    if actS[vname] ~= nil then vvall = actS[vname]
                    else sys.error(elin, 'c', 'Unable to convert a nonexistent variable.') end

                    if actB[vname] == nil then
                        
                        if vvall == 'yes' or vvall == 'true' then actB[vname] = true
                        elseif vvall == 'not' or vvall == 'false' then actB[vname] = false   
                        else sys.error(elin, 'c', 'Bucket cannot convert this non boolean value.') end

                        actS[vname] = nil

                    else sys.error(elin, 'c', "You already have a bool with the same name.") end
                end
            
            -- Strange type --
            else sys.error(elin, 'c', 'This is not a default Bucket data type.') end
        end

        -- Round --
        if line:sub(1, 7) == "round: " then
            
            -- Remove keyword --
            mln = line:gsub('round: ', '')

            -- This variable exists --
            if actN[mln] ~= nil then
                
                val = actN[mln]
                val = math.floor(val)

                actN[mln] = val

            else sys.error(elin, 'c', 'This variable does not exist in the current context.') end
        end

        -- Make --
        if line:sub(1, 6) == "make: " then

            -- Remove keyword --
            mln = line:sub(7)

            -- Get all words --
            mln = sys.split(mln, ' ')

            -- Store values --
            var, val, opr = mln[1], mln[3], mln[2]

            -- Value --

            -- The value is a number --
            if isNum(val, actN) then
                
                if actN[val] ~= nil then val = actN[val]
                else val = tonumber(val) end
            
            -- The value is a string --
            elseif isStr(val, actS) then

                if actS[val] ~= nil then val = actS[val]
                else val = val:gsub('\'', '') end

            -- The value is a bool --
            elseif isBol(val, actB) then sys.error(elin, 'c', 'Cannot use a boolean in an operation.')

            -- Strange value --
            else sys.error(elin, 'c', 'Bucket cannot uses this value in a operration.') end
            
            -- Variable type --

            -- The variable is a number --
            if actN[var] ~= nil then actN = make(elin, var, val, opr, actN)
            
            -- The variable is a string --
            elseif actS[var] ~= nil then actS = make(elin, var, val, opr, actS)
            
            -- Errors --
            elseif actB[var] ~= nil then sys.error(elin, 'c', 'Booleans just can be 0 or 1.')
            else sys.error(elin, 'c', 'This variable does not exist.') end
        end

        -- Rise --
        if line:sub(1, 6) == "rise: " then

            -- Remove keywords --
            var = line:gsub('rise: ', '')

            -- If exists add one --
            if actN[var] ~= nil then actN[var] = actN[var] + 1
            else sys.error(elin, 'c', 'Unknow variable.') end
        end

        -- down --
        if line:sub(1, 6) == "down: " then

            -- Remove keywords --
            var = line:gsub('down: ', '')

            -- If exists subtract one --
            if actN[var] ~= nil then actN[var] = actN[var] - 1
            else sys.error(elin, 'c', 'Unknow variable.') end
        end

        -- List functions --

        -- Put value --
        if line:sub(1, 4) == "in: " then
            
            -- Remove keyword --
            mln = line:sub(5)

            -- in: [index] of list set value --
            sidx, lidx = mln:find('%[.+%]')

            -- Get list index --
            index = mln:sub(sidx + 1, lidx - 1)
            mln = mln:gsub('%[' .. index .. '%]', '')

            -- Get new value and list name --
            if mln:find(' put ') ~= nil then split = sys.split(mln, ' put ')
            else sys.error(elin, 's', 'Missing "put" keyword.') end

            lname, ivall = split[1], split[2]

            -- Remove keyword --
            if lname:sub(1, 4) == " of " then lname = lname:sub(5)
            else sys.error(elin, 's', 'Missing "of" keyword.') end

            -- The list exists --
            if actL[lname] ~= nil then

                -- A number list --
                if actL[lname].type == 'num' then

                    if isNum(ivall, actN) == true then

                        if actN[ivall] ~= nil then actL[lname][index] = actN[ivall]
                        else actL[lname][index] = tonumber(ivall) end

                    else sys.error(elin, 'c', 'The value assigned do not match list type.') end
                end

                -- A string list --
                if actL[lname].type == 'str' then

                    if isStr(ivall, actS) == true then

                        if actS[ivall] ~= nil then actL[lname][index] = actS[ivall]
                        else actL[lname][index] = ivall:gsub('\'', '') end

                    else sys.error(elin, 'c', 'The value assigned do not match list type.') end
                end

                -- A bool list --
                if actL[lname].type == 'bol' then

                    if isBol(ivall, actB) == true then

                        if actB[ivall] ~= nil then actL[lname][index] = actB[ivall]
                        else

                            if ivall == 'yes' then actL[lname][index] = true end
                            if ivall == 'not' then actL[lname][index] = false end
                        end

                    else sys.error(elin, 'c', 'The value assigned do not match list type.') end
                end

            -- Unknow list --
            else sys.error(elin, 'c', 'This list does not exist.') end
        end

        -- Give value --
        if line:sub(1, 6) == "give: " then
            
            mln = line:sub(7)

            -- give: list[index] to var --

            -- Get variable and list --
            list, nvar = sys.midle(mln, ' to ')

            -- Get list index --
            fidx, lidx = list:find('%[.+%]')
            indx = list:sub(fidx + 1, lidx - 1)
            rsub = list:sub(fidx, lidx)

            -- Remove index sufix --
            list = list:sub(1, fidx - 1)

            -- Update index --
            if actN[indx] ~= nil then indx = tostring(actN[indx]) end
            if actS[indx] ~= nil then indx = actS[indx] end
            if actB[indx] ~= nil then
                
                if actB[indx] == true then indx = 'yes' end
                if actB[indx] == false then indx = 'not' end
            end

            -- This list exits --
            if actL[list] ~= nil then

                -- The value exits --
                if actL[list][indx] ~= nil then

                    -- Give it to a number --
                    if actL[list].type == 'num' then

                        if actN[nvar] ~= nil then actN[nvar] = actL[list][indx]
                        else sys.error(elin, 'c', 'Your variable data type do not match list type.') end

                    -- Give it to a string --
                    elseif actL[list].type == 'str' then

                        if actS[nvar] ~= nil then actS[nvar] = actL[list][indx]
                        else sys.error(elin, 'c', 'Your variable data type do not match list type.') end
                    
                    -- Give it to a bool --
                    elseif actL[list].type == 'bol' then

                        if actB[nvar] ~= nil then actB[nvar] = actL[list][indx]
                        else sys.error(elin, 'c', 'Your variable data type do not match list type.') end
                    end
                
                else
                    
                    -- None value --
                    if actN[nvar] ~= nil then actN[nvar] = 'nil'
                    elseif actS[nvar] ~= nil then actS[nvar] = 'nil'
                    elseif actB[nvar] ~= nil then actB[nvar] = 'nil'
                    
                    -- Unknow variable --
                    else sys.error(elin, 'c', 'This variable does not exist.') end
                end
            
            -- Unknow list --
            else sys.error(elin, 'c', 'This list does not exit in the current context.') end
        end

        -- Find item in list --
        if line:sub(1, 6) == "find: " then
            
            -- find: item in list to var --
            
            line = line:gsub('find: ', '')
            this = sys.split(line, ' ')

            -- Get values --
            _item = this[1]
            _list = this[3]
            _tvar = this[5]
            
            -- Get value from _item --
            if isStr(_item, actS) == true then

                if actS[_item] ~= nil then _item = actS[_item]
                else _item = _item:gsub("'", '') end

            elseif isNum(_item, actN) == true then

                if actN[_item] ~= nil then _item = tostring(actN[_item]) end

            elseif isBol(_item, actB) == true then

                if actB[_item] ~= nil then
                    
                    if actB[_item] == true then _item = 'yes' end
                    if actB[_item] == false then _item = 'not' end
                end

            else sys.error(elin, 'c', 'Strange asked value.') end

            -- If this list exists --
            if actL[_list] ~= nil then
                
                if actS[_tvar] ~= nil then
                    
                    found = sys.finds(actL[_list], _item)
                    
                    -- Fix nil return --
                    if not found then actS[_tvar] = 'none'
                    else actS[_tvar] = sys.finds(actL[_list], _item) end

                else sys.error(elin, 'c', 'Only string variables suport index return.') end
            
            else sys.error(elin, 'c', 'Unknow list.') end
        end

        -- Loops --
        
        -- For loop --
        if line:sub(1, 4) == 'for ' then
            
            mln = line:sub(5)

            -- for n times if statlement do: --

            word = sys.split(mln, ' ')

            if word[2] ~= 'times' then sys.error(elin, 's', 'Missing keyword "times".') end
            if word[3] ~= 'if' then sys.error(elin, 's', 'Missing keyword "if".') end
            if word[#word] ~= 'do:' then sys.error(elin, 's', 'Missing keyword "do:".') end

            -- Repeat times --
            rnum = word[1]

            -- Logic statlement --
            ifidx = mln:find('if ')
            doidx = mln:find('do:')

            condt = mln:sub(ifidx + 3, doidx - 2)

            -- Update value --
            if isNum(rnum, actN) then
                
                if actN[rnum] ~= nil then rnum = actN[rnum]
                else rnum = math.floor(tonumber(rnum)) end
            
            else sys.error(elin, 'c', 'For loop needs a num value as argument.') end

            -- Find end of loop --
            eidx = 0
            for lidx in pairs(lines) do

                if lines[lidx] == 'end l.' and lidx > clin then

                    eidx = lidx
                    break

                elseif lidx == #lines then sys.error(elin, 's', 'Missing a closing keyword to loop block.') end
            end

            -- Run loop --
            for n = 1, rnum do
                
                if door(elin, condt, actN, actS, actB, actL) == true then

                    for l = clin + 1, eidx - 1 do
                    
                        if _out ~= 'false' or lines[l]:sub(1, 3) == 'end' then _out = run(lines, l, true, name, true) end
                            
                        if _out == 'break' then break end
                        if lines[l]:sub(1, 3) == 'end' then _out = '' end
                    end

                    -- Loop functions --
                    if _out == 'break' then
                        
                        clin = eidx
                        break
                    end
                end
            end
        end

        -- Every loop --
        if line:sub(1, 6) == 'every ' then
            
            mln = line:sub(7)

            -- every item in list do: --

            -- do: --
            if mln:find(' do:') ~= nil and mln:sub(-4) == " do:" then mln = mln:gsub(' do:', '')
            else sys.error(elin, 's', 'Missing keyword "do:".') end

            -- in --
            if not mln:find(' in ') then sys.error(elin, 's', 'Missing keyword "in".') end
            item, list = sys.midle(mln, ' in ')

            -- Find end of loop --
            eidx = 0
            for lidx in pairs(lines) do

                if lines[lidx] == 'end l.' and lidx > clin then

                    eidx = lidx
                    break

                elseif lidx == #lines then sys.error(elin, 's', 'Missing a closing keyword to loop block.') end
            end

            -- Unknow list --
            if actL[list] == nil then sys.error(elin, 'c', 'This list does not exist.')
            
            -- Run for every value --
            else
                
                -- A number list --
                if actL[list].type == 'num' then

                    local _out = ''
                    l_list = sys.dutable(actL[list])
                    l_list.type = nil

                    for i in pairs(l_list) do

                        -- Update value --
                        actN[item] = l_list[i]

                        for l = clin + 1, eidx -1 do

                            if _out ~= 'false' or lines[l]:sub(1, 3) == 'end' then _out = run(lines, l, true, name, true) end
                            if _out == 'break' then break end

                            if lines[l]:sub(1, 3) == 'end' then _out = '' end
                        end

                        -- Loop functions --
                        if _out == 'break' then
                            
                            clin = eidx
                            break
                        end
                    end

                    -- Delete var --
                    actN[item] = nil
                    clin = eidx - 1
                end

                -- A string list --
                if actL[list].type == 'str' then

                    local _out = ''
                    l_list = sys.dutable(actL[list])
                    l_list.type = nil

                    for i in pairs(l_list) do

                        -- Update value --
                        actS[item] = l_list[i]

                        for l = clin + 1, eidx -1 do

                            if _out ~= 'false' or lines[l]:sub(1, 3) == 'end' then _out = run(lines, l, true, name, true) end
                            if _out == 'break' then break end

                            if lines[l]:sub(1, 3) == 'end' then _out = '' end
                        end

                        -- Loop functions --
                        if _out == 'break' then
                            
                            clin = eidx
                            break
                        end
                    end

                    -- Delete var --
                    actS[item] = nil
                    clin = eidx - 1
                end

                -- A bool list --
                if actL[list].type == 'bol' then

                    local _out = ''
                    l_list = sys.dutable(actL[list])
                    l_list.type = nil

                    for i in pairs(l_list) do

                        -- Update value --
                        actB[item] = l_list[i]

                        for l = clin + 1, eidx -1 do

                            if _out ~= 'false' or lines[l]:sub(1, 3) == 'end' then _out = run(lines, l, true, name, true) end
                            if _out == 'break' then break end

                            if lines[l]:sub(1, 3) == 'end' then _out = '' end
                        end

                        -- Loop functions --
                        if _out == 'break' then
                            
                            clin = eidx
                            break
                        end
                    end

                    -- Delete var --
                    actB[item] = nil
                    clin = eidx - 1
                end
            end
        end

        -- While loop --
        if line:sub(1, 6) == 'while ' then
            
            mln = line:sub(7)

            -- while statlement do: --

            word = sys.split(mln, ' ')

            -- Check syntax --
            if word[#word] ~= 'do:' then sys.error(elin, 's', 'Missing keyword "do:".') end

            -- Logic statlement --
            condt = mln:gsub(' do:', '')

            -- Find end of loop --
            eidx = 0
            for lidx in pairs(lines) do

                if lines[lidx] == 'end l.' and lidx > clin then

                    eidx = lidx
                    break

                elseif lidx == #lines then sys.error(elin, 's', 'Missing a closing keyword to loop block.') end
            end
            
            -- Run lines while true --
            while door(elin, condt, actN, actS, actB, actL) == true do

                for l = clin + 1, eidx - 1 do
                
                    if _out ~= 'false' or lines[l]:sub(1, 3) == 'end' then _out = run(lines, l, true, name, true) end
                        
                    if _out == 'break' then break end
                    if lines[l]:sub(1, 3) == 'end' then _out = '' end
                end

                -- Loop functions --
                if _out == 'break' then
                    
                    clin = eidx
                    break
                end
            end

            clin = eidx
        end

        -- Break loop --
        if sub and line == 'break.' then return 'break' end

        -- Task run --

        -- Call --
        if line:sub(1, 6) == "call: " then

            mln = line:gsub('call: ', '')

            -- Fix syntax --
            if lin:find(':') ~= nil then
                    
                if lin:find(': ') ~= nil then lin = lin:gub(': ', ':') end
                if lin:find(' :') ~= nil then lin = lin:gub(' :', ':') end
            end

            -- name:arg to var --
            split = sys.split(mln, ' to ')
            tname = split[1]
            r_var = split[2]

            -- Arg --
            if tname:find(':') ~= nil then
                
                -- Fix task name and get argument --
                split = sys.split(tname, ':')
                tname = split[1]
                t_arg = split[2]
            end

            -- Run task --
            if actT[tname] ~= nil then

                -- Create temporary variable --
                if t_arg ~= nil then

                    if isNum(t_arg, actN) then
                        
                        -- Update value --
                        if actN[t_arg] ~= nil then t_arg = actN[t_arg] end
                        actN[actT[tname].arg] = tonumber(t_arg)
                    end

                    if isStr(t_arg, actS) then
                        
                        -- Update value --
                        if actS[t_arg] ~= nil then t_arg = actS[t_arg] end
                        actS[actT[tname].arg] = t_arg:gsub('\'', '')
                    end

                    if isBol(t_arg, actB) then
                        
                        -- Update value --
                        if actB[t_arg] ~= nil then t_arg = actB[t_arg] end
                        if t_arg == 'yes' then t_arg = true end
                        if t_arg == 'not' then t_arg = false end

                        actB[actT[tname].arg] = t_arg
                    end
                end

                -- Run task lines --
                for i = actT[tname].flin + 1, actT[tname].llin - 1 do
                    
                    rtrn = run(lines, i, true, name, true)
                end

                -- Has a return --
                if rtrn ~= nil and (rtrn ~= 'true' and rtrn ~= 'false') then
                    
                    -- Return to self --
                    if r_var == 'self.' then sys.error(elin, 'c', 'This task returned a value, but there is no variable to assign.')
                    
                    -- To a variable --
                    else

                        -- The task returned a number --
                        if actN[r_var] ~= nil then

                            -- A number returned --
                            if isNum(rtrn, actN) then
                                
                                -- Fix value --
                                if actN[rtrn] ~= nil then actN[r_var] = actN[rtrn]
                                else actN[r_var] = tonumber(rtrn) end
            
                            else sys.error(elin, 'c', 'The return value is not a number.') end
                        
                        -- The task returned a string --
                        elseif actS[r_var] ~= nil then
                        
                            if isStr(rtrn, actS) then
                                
                                -- Fix value --
                                if actS[rtrn] ~= nil then actS[r_var] = actS[rtrn]
                                else actS[r_var] = rtrn:gsub('\'', '') end
                            
                            else sys.error(elin, 'c', 'The return value is not a string.') end
                        
                        -- The task returned a bool --
                        elseif actB[r_var] ~= nil then

                            if isBol(rtrn, actB) then
                                    
                                -- Fix value --
                                if actB[rtrn] ~= nil then actB[r_var] = actB[rtrn]
                                else
                                    
                                    if rtrn == 'yes' then actB[r_var] = true end
                                    if rtrn == 'not' then actB[r_var] = false end
                                end

                            else sys.error(elin, 'c', 'The return value is not a bool.') end

                        -- Strange value --
                        else sys.error(elin, 'c', 'Cannot return to a nonexistent variable.') end
                    end
                
                -- Have no a return --
                elseif r_var ~= 'self.' then sys.error(elin, 'c', 'Your statement requires a return.') end
            
                -- Delete temporary variable --
                actN[actT[tname].arg] = nil
                actS[actT[tname].arg] = nil
                actB[actT[tname].arg] = nil

            -- Unknow task --
            else sys.error(elin, 'c', 'Attempt to call an unassigned task.') end
        end

        -- Return --
        if line:sub(1, 8) == "return: " and sub then
            
            mln = line:gsub('return: ', '')

            -- Return a number --
            if isNum(mln, actN) then
                
                if actN[mln] ~= nil then mln = tostring(actN[mln]) end
                return mln
            
            -- Return a string --
            elseif isStr(mln, actS) then
            
                if actS[mln] ~= nil then mln = "'" .. actS[mln] .. "'" end
                return mln
            
            -- Return a bool --
            elseif isBol(mln, actB) then
                
                if actB[mln] ~= nil then
                    
                    if mln == true then mln = 'yes' end
                    if mln == false then mln = 'not' end
                end
                return mln
            
            -- Strange value --
            else sys.error(elin, 'c', 'Cannot return a unknow value.') end
        end
    
    -- Line out of block --
    elseif enbd and sub ~= true then

        -- Class lines --
        if not (line:sub(1, 1) == '#' or (line:sub(1, 3) == "[to" and line:sub(-1) == "]")) then

            -- Line out of class or function --
            if not oncl then sys.error(elin, 'c', 'Line out of class block.')
            elseif onfc then sys.error(elin, 'c', 'Task out of class block.')
            end
        end
    end

--# Execution stuff ----------------------------------------#--

    -- End script --
    if line == "close." then

        if onfc or ontk then sys.error(elin, 's', 'Missing a closing keyword.')
        else

            oncl = false
            brk = true
        end
    end

    -- No closing class --
    if clin == #lines and oncl then
    
        sys.error(elin, 's', 'Missing "close." keyword to close class block.')
	end
        
    -- Next line --
    if sub ~= true and clin ~= kill then clin = clin + 1
    else return tostring(enbd) end

    -- Recall yourself --
    if not brk and sub ~= true then run(lines, clin, enbd, name) end
end