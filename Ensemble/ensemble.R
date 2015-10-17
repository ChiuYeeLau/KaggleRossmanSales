xgb_1 = read.csv('xgb_1.csv')
xgb_2 = read.csv('xgb_2.csv')
xgb_3 = read.csv('xgb_3.csv')
xgb_4 = read.csv('xgb_4.csv')
xgb_5 = read.csv('xgb_5.csv')
xgb_6 = read.csv('xgb_6.csv')
xgb_7 = read.csv('xgb_7.csv')
xgb_8 = read.csv('xgb_8.csv')
xgb_9 = read.csv('xgb_9.csv')
xgb_10 = read.csv('xgb_10.csv')

xgb_ensemble = data.frame(Id = xgb_1$Id, 
                          Sales = (xgb_1$Sales + 
                                     xgb_2$Sales + 
                                     xgb_3$Sales +
                                     xgb_4$Sales +
                                     xgb_5$Sales +
                                     xgb_6$Sales + 
                                     xgb_7$Sales +
                                     xgb_8$Sales +
                                     xgb_9$Sales +
                                     xgb_10$Sales)/10.0)

xgb_ensemble = data.frame(Id = xgb_1$Id, 
                          Sales = (xgb_6$Sales + 
                                     xgb_7$Sales +
                                     xgb_8$Sales +
                                     xgb_9$Sales +
                                     xgb_10$Sales)/5.0)

write.csv(xgb_ensemble, "xgb_ensemble_5.csv", row.names = FALSE)