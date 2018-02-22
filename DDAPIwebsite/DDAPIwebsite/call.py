# text file parser
# reads in API calls for application

import re


def parse_api_calls(file):

    call_dict = {}
    infile = iter(open(file, 'r'))

    for line in infile:
        params =[]
        if len(line.strip()) == 0 or line[0] == '#':
            pass
        elif line[0] == '@':
            name = re.split(' |\n', line)[1]
            # call = Call(name)
            while True:
                line = next(infile)
                par = re.split(' |\n', line)
                if par[0] == 'param':
                    # call.add_param(par[1], par[2])
                    params.append({par[1]: par[2]})
                else:
                    break
            if line[0] == '?':
                query = re.split('\n', line)[0][2:]
                call_dict[name] = [{'params': params}, {'query': query}]

    return call_dict


def replace_variables(query, params):
    string_arr = query.split(' ')

    for word in string_arr:
        for param, val in params.items():
            temp = '$$' + param + '$$'
            if word == temp:
                query = query.replace(word, str(val))

    return query


calls = parse_api_calls('sampleAPICalls')
replace_variables(calls['hearing_transcript_by_id'][1].get('query'), {'hid': 1})