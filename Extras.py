# for i, row in enumerate(d.test_data):
#     res = test(p_kama, p_rosa, p_can, row)
#     if res == [-1, -1, -1]:
#         result = 0
#         print(result)
#     elif res == [1, -1, -1]:
#         result = 1
#         print(1)
#     elif res == [-1, 1, -1]:
#         result = 2
#         print(result)
#     elif res == [-1, -1, 1]:
#         result = 3
#         print(result)
#     else:
#         print(res)
#
#     if result == d.test_targets[i]:
#         ov_corr += 1

# corr_test = 0
# for i, row in enumerate(d.tr_data):
#     if p_kama.predict(row) == 1:
#         corr_test += 1
# print("kama correct: ", corr_test)


    # for i, row in enumerate(d.tr_data):
    #     p_kama.train(row, d.kama_targ[i])
    # kama_correct_trials.append((p_kama.correct/165)*100)
    # p_kama.correct = 0

    # def clean_kama(self):
    #     list_ = []
    #     for i in range(len(self.targets_or)):
    #         if self.targets_or[i] != 1:
    #             list_.append(-1)
    #         else:
    #             list_.append(1)
    #     return list_

    # def test(p_kama, p_rosa, p_can, inpt):  # takes in the three trained perceptrons and a set of data
    # result = []
    # result.append(p_kama.predict(inpt))
    # result.append(p_rosa.predict(inpt))
    # result.append(p_can.predict(inpt))
    # return result

