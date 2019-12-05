sys = {}

function sys.split(str, div)

    -- Table to store substrings --
    local subs = {}

    -- For every word --
    while true do

        -- Get index of substring (div) --
        local findx, lindx = str:find(div)

        -- Store last substring --
        if not findx then

            subs[#subs + 1] = str
            break
        end

        -- Store the substring before (div) --
        subs[#subs + 1], str = str:sub(1, findx - 1), str:sub(lindx + 1)
    end

    return subs
end

function sys.midle(word, mid)

    if word:find(mid) ~= nil then

        word = sys.split(word, ' ')

        -- After finding keyword, no mater if it has spaces or not --
        if mid:find(' ') then mid = mid:gsub(' ', '') end

        farg = word[sys.finds(word, mid) - 1]
        larg = word[sys.finds(word, mid) + 1]

        return farg, larg
    end
end

function sys.finds(lst, val)

    for itm in pairs(lst) do

        if lst[itm] == val then return itm end
    end
end

function sys.tabletostr(tab)
    
    local cnv = ''

    for it in pairs(tab) do
        
        cnv = cnv .. tostring(tab[it]) .. ', '
    end

    cnv = cnv:sub(1, -3)

    return cnv
end

function sys.error(line, error, message)
    
    -- Update error type --
    if error == "c" then error = "\n\n[Compiler Error] " end
    if error == "s" then error = "\n\n[Syntax Error] " end

    -- Print error --
    print(error .. message .. "\nIn line [" .. line .. "]")
    print("type any key to exit...")
    io.read()

    os.exit()
end

function sys.debug(message, tag)
    
    if type(message) == 'table' then message = sys.tabletostr(message) end
    
    if tag ~= nil then io.write('\ndebug: [' .. tag .. '][' .. tostring(message) .. ']\n')
    else io.write('\ndebug: [' .. tostring(message) .. ']\n') end
end