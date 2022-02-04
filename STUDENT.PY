import  pandas as pd
import statistics
import csv
df=pd.read_csv("StudentsPerformance.csv")
mathscore_list=df["math score"].to_list()
readingscore_list=df["reading score"].to_list()
writingscore_list=df["writing score"].to_list()

mathscore_mean=statistics.mean(mathscore_list)
readingscore_mean=statistics.mean(readingscore_list)
writingscore_mean=statistics.mean(writingscore_list)

mathscore_median=statistics.median(mathscore_list)
readingscore_median=statistics.median(readingscore_list)
writingscore_median=statistics.median(writingscore_list)

mathscore_mode=statistics.mode(mathscore_list)
readingscore_mode=statistics.mode(readingscore_list)
writingscore_mode=statistics.mode(writingscore_list)


print("mean , median, mode of mathscore is {},{} and {}".format(mathscore_mean, mathscore_median, mathscore_mode))
print("mean , median, mode of reading score id is {},{} and {}".format(readingscore_mean, readingscore_median, readingscore_mode))
print("mean , median, mode of writing score is {},{} and {}".format(writingscore_mean, writingscore_median,writingscore_mode))

mathscore_std_deveation=statistics.stdev(mathscore_list)
readingscore_std_deveation=statistics.stdev(readingscore_list)
writingscore_std_deveation=statistics.stdev(writingscore_list)



mathscore_first_std_deviation_start, mathscore_first_std_deviation_end = mathscore_mean-mathscore_std_deveation, mathscore_mean+mathscore_std_deveation
mathscore_second_std_deviation_start, mathscore_second_std_deviation_endd = mathscore_mean-(2*mathscore_std_deveation), mathscore_mean+(2*mathscore_std_deveation)
mathscore_third_std_deviation_start, mathscore_third_std_deviation_endd = mathscore_mean-(3*mathscore_std_deveation), mathscore_mean+(3*mathscore_std_deveation)

writingscore_std_deviation_start, writingscore_first_std_deviation_end = writingscore_mean-writingscore_std_deveation, writingscore_mean+writingscore_std_deveation
writingscore_second_std_deviation_start,writingscore_second_std_deviation_endd = writingscore_mean-(2*writingscore_std_deveation), writingscore_mean+(2*writingscore_std_deveation)
writingscore_third_std_deviation_start, writingscore_third_std_deviation_endd =writingscore_mean-(3*writingscore_std_deveation), writingscore_mean+(3*writingscore_std_deveation)

readingscore_std_deviation_start, readingscore_first_std_deviation_end = readingscore_mean-readingscore_std_deveation,readingscore_mean+readingscore_std_deveation
readingscore_second_std_deviation_start,readingscore_second_std_deviation_endd = readingscore_mean-(2*readingscore_std_deveation), readingscore_mean+(2*readingscore_std_deveation)
readingscore_third_std_deviation_start, readingscorethird_std_deviation_endd =readingscore_mean-(3*readingscore_std_deveation), readingscore_mean+(3*readingscore_std_deveation)

mathscore_list_of_data_within_1_std_deviation = [result for result in mathscore_list if result > mathscore_first_std_deviation_start and result < mathscore_first_std_deviation_end]
mathscore_list_of_data_within_2_std_deviation = [result for result in mathscore_list if result > mathscore_second_std_deviation_start and result < mathscore_second_std_deviation_endd]
mathscore_list_of_data_within_3_std_deviation = [result for result in mathscore_list if result > mathscore_third_std_deviation_start and result < mathscore_third_std_deviation_endd]

writingscore_list_of_data_within_1_std_deviation = [result for result in writingscore_list if result > writingscore_std_deviation_start and result <  writingscore_first_std_deviation_end]
writingscore_list_of_data_within_2_std_deviation = [result for result in writingscore_list if result > writingscore_second_std_deviation_start and result <  writingscore_second_std_deviation_endd]
writingscore_list_of_data_within_3_std_deviation = [result for result in writingscore_list if result > writingscore_third_std_deviation_start and result <  writingscore_third_std_deviation_endd]

readingscore_list_of_data_within_1_std_deviation = [result for result in readingscore_list if result > readingscore_std_deviation_start and result <  readingscore_first_std_deviation_end]
readingscore_list_of_data_within_2_std_deviation = [result for result in readingscore_list if result > readingscore_second_std_deviation_start and result <  readingscore_second_std_deviation_endd]
readingscore_list_of_data_within_3_std_deviation = [result for result in readingscore_list if result > readingscore_third_std_deviation_start and result < readingscorethird_std_deviation_endd]

print("{}% of data for mathscore lies within 1 standard deviation".format(len(mathscore_list_of_data_within_1_std_deviation)*100.0/len(mathscore_list)))
print("{}% of data for mathscore lies within 2 standard deviations".format(len(mathscore_list_of_data_within_2_std_deviation)*100.0/len(mathscore_list)))
print("{}% of data for mathscore lies within 3 standard deviations".format(len(mathscore_list_of_data_within_3_std_deviation)*100.0/len(mathscore_list)))
print("{}% of data for writingscore lies within 1 standard deviation".format(len(writingscore_list_of_data_within_1_std_deviation)*100.0/len(writingscore_list)))
print("{}% of data for writingscore lies mathscore 2 standard deviations".format(len(writingscore_list_of_data_within_1_std_deviation)*100.0/len(writingscore_list)))
print("{}% of data for writingscore lies mathscore 3 standard deviations".format(len(writingscore_list_of_data_within_1_std_deviation)*100.0/len(writingscore_list)))
print("{}% of data for readingscore lies within 1 standard deviation".format(len(readingscore_list_of_data_within_1_std_deviation)*100.0/len(readingscore_list)))
print("{}% of data for readingscore lies mathscore 2 standard deviations".format(len(readingscore_list_of_data_within_1_std_deviation)*100.0/len(readingscore_list)))
print("{}% of data for readingscore lies mathscore 3 standard deviations".format(len(readingscore_list_of_data_within_1_std_deviation)*100.0/len(readingscore_list)))