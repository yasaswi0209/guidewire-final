import { View, Text, TextInput, Pressable, StyleSheet } from "react-native";
import { useState } from "react";

export default function Risk(){

  const [weather,setWeather] = useState("");
  const [aqi,setAqi] = useState("");
  const [risk,setRisk] = useState("");
  const [reason,setReason] = useState("");

  function calculate(){

    if(weather==="rain" && Number(aqi)>150){

      setRisk("High");
      setReason("Heavy rain + high pollution");

    }

    else if(weather==="heat"){

      setRisk("Medium");
      setReason("Extreme heat conditions");

    }

    else{

      setRisk("Low");
      setReason("Normal conditions");

    }

  }


  return(

    <View style={styles.container}>

      <Text style={styles.title}>
        AI Risk Analysis
      </Text>


      <TextInput
        placeholder="Weather (rain/heat)"
        value={weather}
        onChangeText={setWeather}
        style={styles.input}
      />


      <TextInput
        placeholder="AQI"
        value={aqi}
        onChangeText={setAqi}
        style={styles.input}
      />


      <Pressable
        onPress={calculate}
        style={styles.button}
      >

        <Text style={styles.buttonText}>
          Analyze Risk
        </Text>

      </Pressable>


      {risk && (

        <View style={styles.result}>

          <Text>
            Risk Level
          </Text>

          <Text style={styles.big}>
            {risk}
          </Text>

          <Text>
            {reason}
          </Text>

        </View>

      )}

    </View>

  )

}


const styles = StyleSheet.create({

  container:{
    padding:20
  },

  title:{
    fontSize:24,
    fontWeight:"bold"
  },

  input:{
    borderWidth:1,
    marginTop:15,
    padding:10,
    borderRadius:8
  },

  button:{
    backgroundColor:"#6366f1",
    padding:15,
    marginTop:15,
    borderRadius:10
  },

  buttonText:{
    color:"#fff"
  },

  result:{
    marginTop:20,
    padding:18,
    backgroundColor:"#eef2ff",
    borderRadius:12
  },

  big:{
    fontSize:28,
    fontWeight:"bold"
  }

});