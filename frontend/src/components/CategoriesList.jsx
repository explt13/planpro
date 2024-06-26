import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React, { useContext, useEffect, useMemo, useState } from 'react'
import UserContext from '../context/UserContext'
import { useNavigate } from 'react-router-dom'
import classes from './styles/Categories.module.css'
import Alert from './UI/Alert/Alert'


const CategoriesList = ({all, withQty, size, ...props}) => {
    const {setAlertResponse, eventCategories} = useContext(UserContext)

    const handleSelect = (ev, name) => {
        
        if (props.interests.includes(name)){
            ev.currentTarget.classList.remove(classes.active) //HERE
            props.onCategoryClick(props.interests.filter(c => c !== name))
        
        } else {
            if (props.canAdd){
                ev.currentTarget.classList.add(classes.active)
                props.onCategoryClick(prevSelected => [...prevSelected, name])
            } else if (!props.canAdd){
                setAlertResponse({status: 409, text: 'You\'ve already added 5 categories'})
            }
            
        }
    
        
    }

    
    const sortedEventCategories = useMemo(() => {
        return [...eventCategories].sort((a, b) => b.qty - a.qty)
    }, [eventCategories])
        
    const navigate = useNavigate()

    return (
        <div className={[classes.categories, all ? classes.all : undefined].join(' ')}>
            {(all ? sortedEventCategories : sortedEventCategories.slice(0, 4)).map((category) => {
                let found;
                if (props.interests){
                    found = props.interests.find(i => i === category.value)
                }
                return (
                
                <div
                className={[found ? classes.active : undefined, size ? classes[size]: undefined, classes.category, classes[category.className]].join(' ')}
                key={category.name}
                onClick={props.choose ? (ev) => handleSelect(ev, category.value) : () => navigate('/map', {state: {action: 'selectCategory', category: category.value}})}>
                    <div className={classes.categoryIcon}><FontAwesomeIcon icon={category.icon}/></div>
                    <div className={classes.categoryName}>{category.name}</div>
                    {withQty &&
                    <div className={classes.qty}>{category.qty}</div>
                    }
                </div>
               
            )})}
        </div>
    )
}

export default CategoriesList