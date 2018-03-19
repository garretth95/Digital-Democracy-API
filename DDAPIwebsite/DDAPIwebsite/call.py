# text file parser
# reads in API calls for application
# created by Garrett Heald

import re


# parses text file that contains all API calls to be used by the server
def parse_api_calls(myfile):

    call_dict = {}
    infile = iter(open(myfile, 'r'))

    for line in infile:
        params = {}
        if len(line.strip()) == 0 or line[0] == '#':
            pass
        elif line[0] == '@':
            name = re.split(' |\n', line)[1]
            while True:
                line = next(infile)
                par = re.split(' |\n', line)
                if par[0] == 'param':
                    params.update({par[1]: par[2]})
                else:
                    break
            if line[0] == '?':
                query = re.split('\n', line)[0][2:]
                call_dict[name] = {'params': params, 'query': query}

    return call_dict


# replaces the $$variables$$ with the correct parameter for SQL query
def replace_variables(query, params, types):
    string_arr = query.split(' ')

    for word in string_arr:
        for param, val in params.items():
            temp = '$$' + param + '$$'
            if word == temp:
                if types[param] == 'String':
                    query = query.replace(word, "'" + str(val) + "'")
                else:
                    query = query.replace(word, str(val))

    return query


