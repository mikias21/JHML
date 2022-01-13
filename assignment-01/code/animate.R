# library
install.packages("ggplot2")
install.packages("dplyr")
install.packages("tidyr")
install.packages("lubridate")
install.packages("gganimate")
install.packages("broom.mixed")


library(ggplot2)
library(dplyr)
library(tidyr)
library(lubridate)
library(gganimate)
library(broom.mixed)

data <- read.csv(file.choose(), header = T)
summary(data)

head(data$date_confirmation)

#handling data

datanew <- data %>%
  mutate(date_confirmation = dmy(date_confirmation))

head(datanew$date_confirmation) # After date format changed

head(data$date_confirmation)    # Before date format changed

#animated time series plota
datanew %>% group_by(date_confirmation) %>% 
  summarise(count = n()) %>% 
  mutate(cuml = cumsum(count)) %>% 
  ggplot(aes(x = date_confirmation, y = cuml)) +
  geom_line(color = 'red') +
  geom_point(size = 1.5) +
  geom_area(fill = 'red') +
  theme_bw() +
  ggtitle('Daily Commulative Cases') +
  transition_reveal(cuml)

# saving animation
anim_save('CumlPlot')

