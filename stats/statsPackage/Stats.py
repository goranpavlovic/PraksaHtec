__author__ = 'vladimir'

import string


def write_file_players():
    with open('input.txt', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                # for i in range(0, list.__len__()):
                #     list[i] = list[i].__str__()
                string_ = "('%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, '%s', '%s')," % \
                          (list[0], list[1], list[2], list[3], list[4], list[5],
                           list[6], list[7], list[8], list[9], list[10])
                output_.write(string_)

# write_file_players()


def write_file_all_star():
    with open('player_allstar.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "(%s, '%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s), \n" % \
                          (list[1], list[0], list[2], list[3], list[4], list[7], list[8],
                           list[9], list[10], list[11], list[12], list[13], list[14], list[15])
                output_.write(string_)


def write_file_career():
    with open('player_career.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "('%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s),\n" % \
                          (list[0], list[1], list[2], list[4], list[5], list[6], list[7],
                           list[8], list[9], list[10], list[11], list[12], list[13])
                output_.write(string_)


# write_file_career()
# write_file_all_star()

def write_file_team():
    with open('teams.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "('%s', '%s', '%s', '%s')," % \
                          (list[0], list[1], list[2], list[3])
                output_.write(string_)

# write_file_team()


def write_file_team_s():
    with open('team_season.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "('%s', %s, '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                          " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                          " %s, %s, %s, %s, %s, %s, %s, %s, %s)," % \
                          (list[0], list[1], list[2], list[3], list[4], list[5], list[6],
                           list[7], list[8], list[9], list[10], list[11], list[12], list[13],
                           list[14], list[15], list[16], list[17], list[18], list[19], list[20],
                           list[21], list[22], list[23], list[24], list[25], list[26], list[27],
                           list[28], list[29], list[30], list[31], list[32], list[33], list[34],
                           list[35])
                output_.write(string_)

# write_file_team_s()


def write_file_coach():
    with open('coaches_data.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "('%s', %s, '%s', '%s', %s, %s, %s, %s, '%s')," % \
                          (list[0], list[1], list[3], list[4],
                           list[5], list[6], list[7], list[8], list[9])
                output_.write(string_)

# write_file_coach()


def write_file_coach_c():
    with open('coaches_career.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "('%s', '%s', '%s', %s, %s, %s, %s)," % \
                          (list[0], list[1], list[2], list[3], list[4], list[5], list[6])
                output_.write(string_)


# write_file_coach_c()

def write_file_reg_season():
    with open('player_playoffs.csv', 'r') as input_:
        with open('output.txt', 'w') as output_:
            for item in input_:
                list = item.split(',')
                string_ = "('%s', '%s', '%s', %s, '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s),\n" % \
                          (list[0], list[2], list[3], list[1], list[4], list[6], list[7],
                           list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15])
                output_.write(string_)


write_file_reg_season()