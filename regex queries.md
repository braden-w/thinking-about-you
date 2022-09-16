# Regex Queries

```regex
     ("properties": \{
       "timestamp": \{
         "__datatype__": "timestamp",
         "value": \{ .* \}
       \}
     \}),
     ("location": \{
       "__datatype__": "geopoint",
       "value": \{[.\s\S]*?\}
   \})
```

```regex
$2,
$1
```

```regex
     "geometry": \{
       "type": "Point",
       "coordinates": null
     \},
     "location": \{
       "__datatype__": "geopoint",
       "value": \{([.\s\S]*?)\}
     \},

     "geometry": \{
       "type": "Point",
       "coordinates": [$1]
     \},
     "location": \{
       "__datatype__": "geopoint",
       "value": $1
     \},
```

```regex
\[(.+), (.+)\]
```

```regex
[$2, $1]
```


```js
newFeatures = geoJSON.features.map((feature) => ({...feature, properties: {timestamp: new Date(feature.properties.timestamp._seconds)}}))
```