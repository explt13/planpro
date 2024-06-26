import React, { useContext, useEffect, useState } from 'react'
import UserContext from '../context/UserContext'
import classes from './styles/ProfileInformation.module.css'
import { Link, useParams } from 'react-router-dom'
import FriendService from '../API/FriendService'
import CustomButton from './UI/CustomButton/CustomButton'
import AuthContext from '../context/AuthContext'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import { faCheck, faUserPen } from '@fortawesome/free-solid-svg-icons'
import CustomCancelButton from './UI/CustomButton/CustomCancelButton'



const ProfileInformation = ({user}) => {
    const {thisUser, setAlertResponse, friends, setFriends, sentFriendRequests, setSentFriendRequests} = useContext(UserContext)
    const { csrftoken } = useContext(AuthContext)

    
    const handleAddFriend = async () => {

        const response = await FriendService.sendFriendRequest(user.username, csrftoken)
        setSentFriendRequests(prevRequests => [...prevRequests, response.data.user])
        setAlertResponse({status: response.status, text: response.data.alert})
    }

    const isThisUser = thisUser.username === user.username
    const isPending = sentFriendRequests.find(friend => friend.username === user.username)
    const isFriend = friends.find(friend => friend.username === user.username)

    const deleteFriend = async () => {
        const response = await FriendService.deleteFriend(thisUser.username, user.username, csrftoken)
        setFriends(friends.filter(friend => friend.username !== user.username))
        setAlertResponse({status: response.status, text: response.data})
    }
    
    return (
        <div className={classes.profileInformationContainer}>
            <div className={classes.mainInformation}>
                <div className={classes.imgContainer}><img src={`http://127.0.0.1:8000/${user.profile_pic}`}></img></div>
                <div className={classes.userInformation}>
                    <div className={classes.fullName}>
                        <div>{user.first_name}</div>
                        <div>{user.last_name}</div>
                    </div>
                    <div className={classes.userUsername}>{user.username}</div>
                    
                    <div className={classes.userAbout}>{user.about && 'About:' }<div>{user.about}</div></div>

                </div>
            </div>
            <div className={classes.options}>
                {isThisUser && <CustomButton className={classes.editProfile}><Link to={`/user/${thisUser.username}/edit`}><span>Edit profile</span> <FontAwesomeIcon icon={faUserPen} /></Link></CustomButton>}
                {isPending && <div className={classes.pending}>pending</div>}
                {isFriend &&
                <div className={classes.alreadyFriends}>
                <div className={classes.friendsLabel}>friends <FontAwesomeIcon icon={faCheck}/></div>
                <CustomCancelButton onClick={deleteFriend} className={classes.deleteFriend}>Unfriend</CustomCancelButton>
                </div>
                }
                {!isThisUser && !isPending && !isFriend &&
                <CustomButton className={classes.addFriend} onClick={handleAddFriend}>Add friend</CustomButton>
                }
            </div>
        </div>
 
    )
}

export default ProfileInformation