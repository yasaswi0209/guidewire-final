import { View, Text, Pressable, StyleSheet } from "react-native";
import { useState } from "react";
import { Picker } from "@react-native-picker/picker";

export default function Claims(){

  const [selected,setSelected] = useState("");
  const [status,setStatus] = useState("");
  const [payout,setPayout] = useState<number | null>(null);
  const [reason,setReason] = useState("");

  function applyClaim(){

    if(!selected){

      setStatus("error");
      setReason("Please select disruption");
      return;

    }

    setStatus("checking");

    setTimeout(()=>{

      const weeklyIncome = 4200;

      const hourlyIncome = weeklyIncome / 7 / 8;

      let hoursLost = 0;
      let reasonText = "";

      if(selected==="rain"){
        hoursLost = 3;
        reasonText = "Heavy Rain Verified";
      }

      else if(selected==="pollution"){
        hoursLost = 2;
        reasonText = "High Pollution Verified";
      }

      else if(selected==="heat"){
        hoursLost = 4;
        reasonText = "Extreme Heat Verified";
      }

      else if(selected==="curfew"){
        setStatus("rejected");
        setReason("No matching disruption");
        return;
      }

      let loss = hourlyIncome * hoursLost;
      loss *= 2;

      setPayout(Math.round(loss));
      setReason(reasonText);
      setStatus("approved");

    },1500);

  }


  return(

    <View style={styles.container}>

      <Text style={styles.title}>
        Claims
      </Text>


      <Text style={styles.label}>
        Select Disruption
      </Text>


      <View style={styles.dropdown}>

        <Picker
          selectedValue={selected}
          onValueChange={(itemValue)=>setSelected(itemValue)}
        >

          <Picker.Item label="Choose option" value="" />

          <Picker.Item label="Heavy Rain" value="rain" />

          <Picker.Item label="High Pollution" value="pollution" />

          <Picker.Item label="Extreme Heat" value="heat" />

          <Picker.Item label="Curfew" value="curfew" />

        </Picker>

      </View>


      <Pressable
        onPress={applyClaim}
        style={styles.button}
      >

        <Text style={styles.buttonText}>
          Apply Claim
        </Text>

      </Pressable>


      {status==="checking" && (

        <Text style={styles.info}>
          Processing claim...
        </Text>

      )}


      {status==="error" && (

        <Text style={styles.error}>
          {reason}
        </Text>

      )}


      {status==="rejected" && (

        <Text style={styles.error}>
          {reason}
        </Text>

      )}


      {status==="approved" && (

        <View style={styles.success}>

          <Text>
            {reason}
          </Text>

          <Text style={styles.big}>
            ₹{payout}
          </Text>

          <Text>
            Approved via UPI
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

  label:{
    marginTop:20,
    fontWeight:"bold"
  },

  dropdown:{
    borderWidth:1,
    borderRadius:10,
    marginTop:10
  },

  button:{
    backgroundColor:"#6366f1",
    padding:15,
    borderRadius:10,
    marginTop:20
  },

  buttonText:{
    color:"#fff"
  },

  info:{
    marginTop:15
  },

  error:{
    marginTop:15,
    color:"red"
  },

  success:{
    marginTop:20,
    padding:18,
    backgroundColor:"#dcfce7",
    borderRadius:12
  },

  big:{
    fontSize:24,
    fontWeight:"bold"
  }

});