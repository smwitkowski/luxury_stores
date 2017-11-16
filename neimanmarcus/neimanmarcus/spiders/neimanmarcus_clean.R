library(readr)
library(stringr)
library(dplyr)
library(lubridate)

setwd("C:\\Users\\switkowski\\Documents\\FreeLance\\luxury_stores\\neimanmarcus\\neimanmarcus\\spiders")

df <- read_csv("./Neiman_Marcus_Stores.csv")


df <- as.data.frame(sapply(df,gsub,pattern="\n",replacement=""))
df <- as.data.frame(sapply(df,gsub,pattern="\r",replacement=""))
df <- as.data.frame(sapply(df,gsub,pattern="\t",replacement=""))
df <- as.data.frame(sapply(df,gsub,pattern="\\[",replacement=""))
df <- as.data.frame(sapply(df,gsub,pattern="\\]",replacement=""))
df <- as.data.frame(sapply(df,gsub,pattern="'",replacement=""))
df$URL <- gsub("?geoLocation=Upper%20Marlboro%20,%20MD&prev=strDir", "", df$URL)
df$Address <- gsub(",","", df$Address)
df$Address <- gsub("\\\\r","", df$Address)
df$Address <- gsub("\\\\n","", df$Address)
df$Address <- gsub("\\\\t","", df$Address)


df$Monday_Open <- format(strptime(df$Monday_Open, "%H:%M"), "%I:%M %p")
df$Monday_Close <- format(strptime(df$Monday_Close, "%H:%M"), "%I:%M %p")
df$Tuesday_Open <- format(strptime(df$Tuesday_Open, "%H:%M"), "%I:%M %p")
df$Tuesday_Close <- format(strptime(df$Tuesday_Close, "%H:%M"), "%I:%M %p")
df$Wednesday_Open <- format(strptime(df$Wednesday_Open, "%H:%M"), "%I:%M %p")
df$Wednesday_Close <- format(strptime(df$Wednesday_Close, "%H:%M"), "%I:%M %p")
df$Thursday_Open <- format(strptime(df$Thursday_Open, "%H:%M"), "%I:%M %p")
df$Thursday_Close <- format(strptime(df$Thursday_Close, "%H:%M"), "%I:%M %p")
df$Friday_Open <- format(strptime(df$Friday_Open, "%H:%M"), "%I:%M %p")
df$Friday_Close <- format(strptime(df$Friday_Close, "%H:%M"), "%I:%M %p")
df$Saturday_Open <- format(strptime(df$Saturday_Open, "%H:%M"), "%I:%M %p")
df$Saturday_Close <- format(strptime(df$Saturday_Close, "%H:%M"), "%I:%M %p")

df$Store_Name <- "Neiman Marcus"

df <- df %>%
  select("Store_Name","Name", "Address", "City", "State", "Zip", "Manager", "Telephone_1", "Telephone_2",
         "Monday_Open",	"Monday_Close",	"Tuesday_Open",	"Tuesday_Close",	"Wednesday_Open",
         "Wednesday_Close",	"Thursday_Open",	"Thursday_Close",	"Friday_Open",	"Friday_Close",
         "Saturday_Open",	"Saturday_Close",	"Sunday_Open",	"Sunday_Close",	"Image_URL",	"URL"
  )

telephone_1 <- ifelse(str_detect(df$Telephone_1, "\\d{3}.\\d{3}.\\d{4}"),
                      paste("(", str_extract(df$Telephone_1, "\\d{3}"), ")", str_extract(df$Telephone_1, "(?<=\\d{3}.)\\d{3}"), "-", str_extract(df$Telephone_1, "\\d{4}"), sep = ""),
                      df$Telephone_1)

telephone_2 <- ifelse(str_detect(df$telephone_2, "\\d{3}.\\d{3}.\\d{4}"),
                      paste("(", str_extract(df$telephone_2, "\\d{3}"), ")", str_extract(df$telephone_2, "(?<=\\d{3}.)\\d{3}"), "-", str_extract(df$telephone_2, "\\d{4}"), sep = ""),
                      df$telephone_2)

df$Telephone_1 <- telephone_1

df$Telephone_2 <- telephone_2

df <- df %>%
  mutate_all(as.character)

df[df == "None"] <- "NA"
df[is.na(df)] <- "NA"

write.csv(df, "./Neiman_Marcus_Stores.csv")
