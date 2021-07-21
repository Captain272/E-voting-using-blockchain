pragma solidity ^0.6.4;
pragma experimental ABIEncoderV2;

contract voting{

    
    struct voter{
        address id;
        string name;
        uint256 addhar;
        bool voted;
        uint8 age;
        
    }
    
    struct candidate{
        address id;
        string name;
        uint256 addhar;
        uint8 age;
        uint256 votes;
        
    }
    address[] public cand;
    string[] public st;
    uint32[] public vot;
    uint256 public j;
    // voter[] public voter_list;
    // candidate[] public candidate_list;
    // constructor (address[] memory can)public{
    //     cand=can;
    // }
    mapping(address=>voter) voters;
    mapping(address=>candidate) candidates;
    function add_candidate(string memory name,uint256 addhar,uint8 age,address add) public returns(string memory){

        if(candidates[add].id==add){
            return ("already registered");
        }
        candidates[add].name=name;
        candidates[add].addhar=addhar;
        candidates[add].age=age;
        candidates[add].id=add;
        cand.push(add);
        return("Done");
    }
    
    
    
     function add_voter(string memory name,uint256 addhar,uint8 age,address add) public returns(string memory){
        if(voters[add].id==add){
            return("Already Registered");
        }
        voters[add].name=name;
        voters[add].addhar=addhar;
        voters[add].age=age;
        voters[add].id=add;
        voters[add].voted=false;
        return("Succesfully Registered");
    }
    
    
    function vote(address voteFor,address add)public returns(string memory){
        if(voters[add].voted==true)
        {
            return("Already voted");
        }
        
        else if(voters[add].age<18)
        {
            return("Age restricted");
        }
        else if(candidates[voteFor].addhar==voters[add].addhar){
            return("You Can't vote yourself");
        }
        voters[add].voted=true;
        candidates[voteFor].votes++;
        return ("Vote-Succesful");
        
    }
    
    function Result()  public returns(string[] memory){
        for(uint i=0;i<cand.length;i++)
        {
            if(candidates[cand[i]].votes>j){
                j=candidates[cand[i]].votes;
            }
        }
        
        for(uint i=0;i<cand.length;i++)
        {
            if(candidates[cand[i]].votes==j)
            {
                st.push(candidates[cand[i]].name);
            }
        }
        return(st);
        }
        
        function winnerdis()public{
            for(uint32 i=0;i<cand.length;i++)
            {
                j=(candidates[cand[i]].votes);
            }
            // j=candidates[cand[0]].votes++;
        }
            
        }
