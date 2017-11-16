library(readr)
library(stringr)
library(dplyr)
library(lubridate)
library(xlsx)

setwd("C:\\Users\\switkowski\\Documents\\FreeLance\\luxury_stores\\bloomingdales\\bloomingdales\\spiders")

df <- read_csv("./Bloomingdales_Stores.csv")

df <- df[is.na(df$Address) == FALSE,]


Monday_Open <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Monday_Open[x], guess_formats(df$Monday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Monday_Close <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Monday_Close[x], guess_formats(df$Monday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Tuesday_Open <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Tuesday_Open[x], guess_formats(df$Tuesday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Tuesday_Close <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Tuesday_Close[x], guess_formats(df$Tuesday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Wednesday_Open <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Wednesday_Open[x], guess_formats(df$Wednesday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Wednesday_Close <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Wednesday_Close[x], guess_formats(df$Wednesday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Thursday_Open <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Thursday_Open[x], guess_formats(df$Thursday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Thursday_Close <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Thursday_Close[x], guess_formats(df$Thursday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Friday_Open <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Friday_Open[x], guess_formats(df$Friday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Friday_Close <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Friday_Close[x], guess_formats(df$Friday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Saturday_Open <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Saturday_Open[x], guess_formats(df$Saturday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Saturday_Close <- lapply(1:nrow(df), function(x){format(parse_date_time(df$Saturday_Close[x], guess_formats(df$Saturday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")})
Sunday_Open <- lapply(1:nrow(df), function(x){if (is.na(df$Sunday_Open[x]) == TRUE){"Closed"} else {format(parse_date_time(df$Sunday_Open[x], guess_formats(df$Sunday_Open[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")}})
Sunday_Close <- lapply(1:nrow(df), function(x){if (is.na(df$Sunday_Close[x]) == TRUE){"Closed"} else {format(parse_date_time(df$Sunday_Close[x], guess_formats(df$Sunday_Close[x], orders = c('hp', 'hms','hmp'))[1][[1]]), "%H:%M")}})

df$Monday_Open <- format(strptime(Monday_Open, "%H:%M"), "%I:%M %p")
df$Monday_Close <- format(strptime(Monday_Close, "%H:%M"), "%I:%M %p")
df$Tuesday_Open <- format(strptime(Tuesday_Open, "%H:%M"), "%I:%M %p")
df$Tuesday_Close <- format(strptime(Tuesday_Close, "%H:%M"), "%I:%M %p")
df$Wednesday_Open <- format(strptime(Wednesday_Open, "%H:%M"), "%I:%M %p")
df$Wednesday_Close <- format(strptime(Wednesday_Close, "%H:%M"), "%I:%M %p")
df$Thursday_Open <- format(strptime(Thursday_Open, "%H:%M"), "%I:%M %p")
df$Thursday_Close <- format(strptime(Thursday_Close, "%H:%M"), "%I:%M %p")
df$Friday_Open <- format(strptime(Friday_Open, "%H:%M"), "%I:%M %p")
df$Friday_Close <- format(strptime(Friday_Close, "%H:%M"), "%I:%M %p")
df$Saturday_Open <- format(strptime(Saturday_Open, "%H:%M"), "%I:%M %p")
df$Saturday_Close <- format(strptime(Saturday_Close, "%H:%M"), "%I:%M %p")
df$Sunday_Open <- format(strptime(Sunday_Open, "%H:%M"), "%I:%M %p")
df$Sunday_Close <- format(strptime(Sunday_Close, "%H:%M"), "%I:%M %p")

df$Store_Name <- "Bloomingdales"

df <- df %>%
  select("Store_Name","Name", "Address", "City", "State", "Zip", "Manager", "Telephone",
         "Monday_Open",	"Monday_Close",	"Tuesday_Open",	"Tuesday_Close",	"Wednesday_Open",
         "Wednesday_Close",	"Thursday_Open",	"Thursday_Close",	"Friday_Open",	"Friday_Close",
         "Saturday_Open",	"Saturday_Close",	"Sunday_Open",	"Sunday_Close",	"Image_URL",	"URL"
  )

df[,9:22][is.na(df[,9:22])] <- "Closed"
df[is.na(df)] <- "NA"
df[df == "None"] <- "NA"

write.csv(df, "./Bloomingdales_Stores.csv")

